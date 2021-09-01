# Troubleshooting

During OpenCV compilation with CUDA support or AlexeyAB YOLO, some erros can pop-up:

* If the error is related with the OpenCV compilation, saying that NVCC was not found, add the lines below to the `~/.bashrc` file:
```
# CUDA NVCC
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64
```

Source: https://forums.developer.nvidia.com/t/cuda-nvcc-not-found/118068

* If the error is related with the Darknet YOLO compilation, saying that some OpenCV libraries can't be found, add those lines to the `~/.bashrc` file:
```
# OpenCV
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
```
