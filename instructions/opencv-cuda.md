# OpenCV 4.5.0 with CUDA

Adiciona suporte ao CUDA pelo OpenCV utilizado na Jetson Nano. É essencial para mesclar a operação da câmera CSI com softwares que utilizam o CUDA (como o YOLO, por exemplo)

Para Instalar:

```
  mkdir openCV && cd openCV
  wget https://raw.githubusercontent.com/AastaNV/JEP/master/script/install_opencv4.5.0_Jetson.sh
  chmod +x install_opencv4.5.0_Jetson.sh
  ./install_opencv4.5.0_Jetson.sh
```

Observações:
O processo demora aproximadamente 4 horas para completar realizando a compilação na própria Jetson
A versão do OpenCV pode ser alterada no script, porem não é garantido que funcionará
É recomendado que o Swapfile da Jetson seja de no mínimo 4GB (explicado como aumentá-lo no uso da ferramenta jtop )

Fonte: https://forums.developer.nvidia.com/t/unable-to-install-opencv-with-cuda-in-jetson-nano/72994#5337084
