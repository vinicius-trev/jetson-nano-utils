# OpenCV 4.5.0 with CUDA

Add support to CUDA on Jetson Nano OpenCV. It is essential to use OpenCV with GPU acceleration

How to Install:

```
  mkdir openCV && cd openCV
  wget https://raw.githubusercontent.com/AastaNV/JEP/master/script/install_opencv4.5.0_Jetson.sh
  chmod +x install_opencv4.5.0_Jetson.sh
  ./install_opencv4.5.0_Jetson.sh
```

Notes:
The compilation takes aproximately 4h to complete using the Jetson Nano
The OpenCV version can be changed on the script, but it is not guaranteed that it will work
It is recommended to increase the Jetson Swapfile to at least 4GB (see jetson-stats)

Source: https://forums.developer.nvidia.com/t/unable-to-install-opencv-with-cuda-in-jetson-nano/72994#5337084
