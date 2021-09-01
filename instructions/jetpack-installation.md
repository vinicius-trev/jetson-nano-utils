# JetPack Installation

- Go to the website: https://developer.nvidia.com/embedded/jetpack
- Choose the option to install JetPack using an SD Card
- Choose Jetson Nano configuration (4GB ou 2GB)
- Extract the downloaded file
- Use the [balenaEtcher](https://www.balena.io/etcher/) software to create the bootable SD Card that will be used by the Jetson
- Insert the SD Card, power the Jetson and follow screen instructions
- Remove LibreOffice
```
sudo apt autoremove libreoffice* -y
sudo apt clean
```


