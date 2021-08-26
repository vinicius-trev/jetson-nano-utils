# Módulo backport-iwlwifi

Possui o objetivo de viabilizar o uso da placa PCI-e Wi-Fi AC9260 da intel na Jetson Nano no slot M.2. existente abaixo do módulo. Consiste de um módulo de Kernel

* Para Instalar:
```
git clone https://git.kernel.org/pub/scm/linux/kernel/git/iwlwifi/backport-iwlwifi.git
cd backport-iwlwifi
git checkout release/core52
make defconfig-iwlwifi-public
make -j4
sudo make install
```

Observações:
- É necessário a release estar na versão core52, diferente disso, o driver não funcionará
- Os arquivos para o device driver do dispositivo AC9260 já devem existir no sistema em /lib/firmare/iwlwifi-9260* , caso não existirem é necessário a inserção:
  ```
  git clone git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git
  sudo cp linux-firmware/iwlwifi-9260* /lib/firmware/
  ```
Fonte: https://forums.developer.nvidia.com/t/intel-ac9260-wifi-card-stops-working-after-upgrade-to-jetpack-4-5/167892
