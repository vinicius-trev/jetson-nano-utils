"""
@author Vinicius Trevisan
@brief Python script to record video stream from CSI Camera on NVidia Jetson Nano
@details
* Available modes (based on Raspberry Pi Camera v3): These modes are used to define the recommended bitrate
  * 0: 1280 x 720 @ 60 FPS
  * 1: 1280 x 720 @ 30 FPS
  * 2: 1640 x 1232 @ 30 FPS
  * 3: 1920 x 1080 @ 30 FPS
  * 4: 3280 x 2464 @ 15 FPS

* Available flip modes (based on Pi Camera flat main flat cable / white pointing UP):
  * 0: Normal
  * 1: Rotated left 90 degrees
  * 2: Rotated 180 degrees
  * 3: Rotated right 90 degrees
"""
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

    # Video modes and CLI arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--mode", required=True, default=1, help="Record mode [default=1]."
		            "Available modes are: "
                            "0: 1280 x 720 @ 60 FPS - "
                            "1: 1280 x 720 @ 30 FPS - "
                            "2: 1640 x 1232 @ 30 FPS - "
                            "3: 1920 x 1080 @ 30 FPS - "
                            "4: 3280 x 2464 @ 15 FPS")
    argparser.add_argument("--duration", default=1, help="Record duration in minutes [default=1]")
    argparser.add_argument("--show", default=0, help="Show video feed in 1280 x 720")
    argparser.add_argument("--flip", default=0, help="Image orientation [default=0]")
    args = vars(argparser.parse_args())

    # Parsing video modes (the bitrate is optimized during H265 encoding)
    fps = bitrate = resolution = 0
    if int(args["mode"]) == 0:   # 1280 x 720 @ 60 FPS
        resolution = (1280, 720)
        fps = 60
        bitrate = 5500 * 1024
    elif int(args["mode"]) == 1: # 1280 x 720 @ 30 FPS
        resolution = (1280, 720)
        fps = 30
        bitrate = 3000 * 1024
    elif int(args["mode"]) == 2: # 1640 x 1232 @ 30 FPS
        resolution = (1640, 1232)
        fps = 30
        bitrate = 6000 * 1024
    elif int(args["mode"]) == 3: # 1920 x 1080 @ 30 FPS
        resolution = (1920, 1080)
        fps = 30
        bitrate = 6000 * 1024
    else: # 3280 x 2464 @ 15 FPS
        resolution = (3280, 2464)
        fps = 15
        bitrate = 15000 * 1024

    flip_method = int(args["flip"])
    filepath = "sample_output_%dx%d_%dfps.mp4" % (resolution[0], resolution[1], fps)
    duration = int(args["duration"]) # Minutes

    logging.info("Starting video capture, press 'q' or 'ctrl+c' to exit")
    logging.info("Settings:\nResolution: %dx%d\nFPS: %d\nRecord Time: %d minutes\nShow: %d\nSaved File Path: %s/%s" 
                    % (resolution[0], resolution[1], fps, duration, int(args["show"]), os.getcwd(), filepath)
                )

    # GStreamer Video Capture
    cap = cv2.VideoCapture(
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! " 
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! "
        "appsink"
        % (resolution[0], resolution[1], fps, flip_method, resolution[0], resolution[1]), cv2.CAP_GSTREAMER)

    # Video File opening with GStreamer
    out = cv2.VideoWriter(
        "appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw, format=RGBA,  framerate=(fraction)%d/1 ! "
        "nvvidconv ! nvv4l2h265enc control-rate=1 bitrate=%d EnableTwopassCBR=1 ! h265parse ! qtmux !"
        "filesink location=%s" % (fps, bitrate, filepath),
        cv2.CAP_GSTREAMER, 0, float(fps), resolution, True)

    # Execution Loop
    if not out.isOpened():
        logging.info("Failed to open output")
        exit()

    start_time = time.time()
    if cap.isOpened():

        if int(args["show"]) == 1:
            cv2.namedWindow("Record Feedback", cv2.WINDOW_AUTOSIZE)

        while int(time.time() - start_time) < int(duration * 60):
            try:
                _, img = cap.read()
                out.write(img)

                if int(args["show"]) == 1:
                    cv2.imshow('Record Feedback', cv2.resize(img, (1280, 720), interpolation = cv2.INTER_AREA))

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            except KeyboardInterrupt:
                break
    else:
        logging.info("Failed to open camera")

    cap.release()
    out.release()
    if int(args["show"]) == 1:
        cv2.destroyAllWindows()

    logging.info("Finished video capture\nElapsed time: %dmin %ds \nFile size: %fMB" 
                    % (((time.time() - start_time) / 60), ((time.time() - start_time) % 60), 
                    (os.path.getsize(filepath) / 1024.0 / 1024.0))
                )
