# Troubleshooting

Podem ocorrer alguns erros durante a compilação do OpenCV com suporte ao CUDA e do YOLO em C. São eles:

* Caso ocorrer erro de compilação do OpenCV com suporte ao CUDA, em que o NVCC não foi encontrado, adicionar ao final do ~/.bashrc:
```
# CUDA NVCC
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64
```

Fonte: https://forums.developer.nvidia.com/t/cuda-nvcc-not-found/118068

* Caso ocorrer erro de execução do YOLO Darknet indicando que as bibliotecas do OpenCV não foram encontradas, adicionar ao final do ~/.bashrc:
```
# OpenCV
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
```
