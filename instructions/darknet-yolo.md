# Darknet YOLO - AlexeyAB

Implementação do YOLO v4 em C segundo o paper original com wrapper / API em python.

* Para Instalar:
    * (1) Realizar o download do código fonte
    ```
    git clone https://github.com/AlexeyAB/darknet.git
    cd darknet
    ```

    * (2) Editar Makefile
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

  * (3) Realizar o build do executavel
    ```
    make -j4
    ```
    
   * (4) Download dos pesos pré-treinados em https://github.com/AlexeyAB/darknet/releases/tag/darknet_yolo_v4_pre
   
* Para executar os exemplos seguir o tutorial: https://github.com/AlexeyAB/darknet#how-to-use-on-the-command-line
* Para executar com a Pi Camera conectada ao conector CSI, utilizar o gstreamer, substituindo o argumento `-c 0`  por `nvarguscamerasrc ! video/x-raw(memory:NVMM),width=640, height=360, framerate=30/1, format=NV12 ! nvvidconv ! video/x-raw, format=BGRx, width=640, height=360 ! videoconvert ! video/x-raw, format=BGR ! appsink`

  Exemplos:
  ```
  # YOLO-V4 (COCO)
  ./darknet detector demo cfg/coco.data cfg/yolov4.cfg weights/yolov4.weights "nvarguscamerasrc ! video/x-raw(memory:NVMM),width=640, height=360, framerate=30/1, format=NV12 ! nvvidconv ! video/x-raw, format=BGRx, width=640, height=360 ! videoconvert ! video/x-raw, format=BGR ! appsink" -dont_show

  # YOLO-V4-tiny (COCO)
  ./darknet detector demo cfg/coco.data cfg/yolov4-tiny.cfg weights/yolov4-tiny.weights "nvarguscamerasrc ! video/x-raw(memory:NVMM),width=640, height=360, framerate=30/1, format=NV12 ! nvvidconv ! video/x-raw, format=BGRx, width=640, height=360 ! videoconvert ! video/x-raw, format=BGR ! appsink" -dont_show
  ```
  
* Exemplos do uso do YOLO Darknet com wrapper em python
    * https://github.com/AlexeyAB/darknet/blob/master/darknet.py
    * https://github.com/AlexeyAB/darknet/blob/master/darknet_video.py

Fontes: \
https://jkjung-avt.github.io/yolov4/ \
https://github.com/AlexeyAB/darknet

 
