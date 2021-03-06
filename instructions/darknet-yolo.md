# Darknet YOLO - AlexeyAB

YOLO v4 implementation in C, as defined on the original paper with a wrapper / API in python.

* How to Install:
    * (1) Download source code
    ```
    git clone https://github.com/AlexeyAB/darknet.git
    cd darknet
    ```

    * (2) Modify the Makefile
    ```
    GPU=1
    CUDNN=1
    CUDNN_HALF=1
    OPENCV=1
    AVX=0
    OPENMP=1
    LIBSO=1
    ZED_CAMERA=0
    ZED_CAMERA_v2_8=0

    ......

    USE_CPP=0
    DEBUG=0

    ARCH= -gencode arch=compute_53,code=[sm_53,compute_53]
    ```

  * (3) Build the darknet executable
    ```
    make -j4
    ```
    
   * (4) Download pre trained weights on https://github.com/AlexeyAB/darknet/releases/tag/darknet_yolo_v4_pre
   
* To execute the examples, follow the commands on: https://github.com/AlexeyAB/darknet#how-to-use-on-the-command-line
* To execute using the Pi Camera, replace the `-c 0` argument with a GStreamer pipeline `nvarguscamerasrc ! video/x-raw(memory:NVMM),width=640, height=360, framerate=30/1, format=NV12 ! nvvidconv ! video/x-raw, format=BGRx, width=640, height=360 ! videoconvert ! video/x-raw, format=BGR ! appsink`

  Examples:
  ```
  # YOLO-V4 (COCO)
  ./darknet detector demo cfg/coco.data cfg/yolov4.cfg weights/yolov4.weights "nvarguscamerasrc ! video/x-raw(memory:NVMM),width=640, height=360, framerate=30/1, format=NV12 ! nvvidconv ! video/x-raw, format=BGRx, width=640, height=360 ! videoconvert ! video/x-raw, format=BGR ! appsink" -dont_show

  # YOLO-V4-tiny (COCO)
  ./darknet detector demo cfg/coco.data cfg/yolov4-tiny.cfg weights/yolov4-tiny.weights "nvarguscamerasrc ! video/x-raw(memory:NVMM),width=640, height=360, framerate=30/1, format=NV12 ! nvvidconv ! video/x-raw, format=BGRx, width=640, height=360 ! videoconvert ! video/x-raw, format=BGR ! appsink" -dont_show
  ```
  
* C API Examples showing how to use darknet on python
    * https://github.com/AlexeyAB/darknet/blob/master/darknet.py
    * https://github.com/AlexeyAB/darknet/blob/master/darknet_video.py

Sources: \
https://jkjung-avt.github.io/yolov4/ \
https://github.com/AlexeyAB/darknet

 
