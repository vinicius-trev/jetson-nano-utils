import sys
import cv2
import gi
import os
import time
import logging
import argparse

gi.require_version('Gst', '1.0')
from gi.repository import Gst

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Video settings and CLI arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-f", "--fps", required=True, help="Video Frame Rate per Second")
    argparser.add_argument("-x", "--width", required=True, help="Resolution Width")
    argparser.add_argument("-y", "--height", required=True, help="Resolution Height")
    argparser.add_argument("-d", "--duration", required=True, help="Record Duration in Minutes")
    argparser.add_argument("-s", "--show", required=True, help="Show Video Feed")
    argparser.add_argument("-p", "--flip_method", default=0, help="Image Orientation")
    args = vars(argparser.parse_args())

    flip_method = int(args["flip_method"])
    resolution = (int(args["width"]), int(args["height"]))
    fps = int(args["fps"])
    filepath = "sample_output_%dx%d_%dfps.mkv" % (resolution[0], resolution[1], fps)
    video_time = int(args["duration"]) # Minutes

    logging.info("Starting video capture, press 'q' to exit")
    logging.info("Settings:\nResolution: %dx%d\nFPS: %d\nRecord Time: %d minutes\nShow: %d\nSaved File Path: %s/%s" % (resolution[0], resolution[1], fps, video_time, int(args["show"]), os.getcwd(), filepath))

    # GStreamer Video Capture
    cap = cv2.VideoCapture(
       "nvarguscamerasrc ! "
       "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! " 
       "nvvidconv flip-method=%d ! " 
       "video/x-raw, format=(string)BGRx ! "
       "videoconvert ! "
       "video/x-raw, format=(string)BGR ! "
       "appsink"
       % (resolution[0], resolution[1], fps, flip_method), cv2.CAP_GSTREAMER)

    # Video File opening with GStreamer
    out = cv2.VideoWriter(
        "appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw,format=RGBA ! nvvidconv ! nvv4l2h264enc ! h264parse ! qtmux !"
        "filesink location=%s" % (filepath),
        cv2.CAP_GSTREAMER, 0, float(fps), resolution, True)

    # Execution Loop
    if not out.isOpened():
        logging.info("Failed to open output")
        exit()
	
    start_time = time.time()
    if cap.isOpened():
        if int(args["show"]) == 1:
            cv2.namedWindow("Record Feedback", cv2.WINDOW_AUTOSIZE)

        while int(time.time() - start_time) < int(video_time * 60):
            try:
                ret_val, img = cap.read();
            
                if int(args["show"]) == 1:
                    cv2.imshow('Record Feedback',img)
    
                out.write(img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            except KeyboardInterrupt:
                break
    else:
        logging.info("Failed to open camera")

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    logging.info("Finished video capture\nElapsed time: %dmin %ds \nFile size: %fMB" % (((time.time() - start_time) / 60), ((time.time() - start_time) % 60), (os.path.getsize(filepath) / 1024.0 / 1024.0)))

