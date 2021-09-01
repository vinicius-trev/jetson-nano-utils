# backport-iwlwifi Kernel Module

It make available the usage of the Wi-Fi PCI-e AC9260 M.2. board on the Jetson Nano

* How to Install:
```
git clone https://git.kernel.org/pub/scm/linux/kernel/git/iwlwifi/backport-iwlwifi.git
cd backport-iwlwifi
git checkout release/core52
sudo make defconfig-iwlwifi-public
make -j4
sudo make install
```

Notes:
- It is necessary to use the core52 release, on a different version the driver will not work
- The Jetson must have the AC9260 device driver files on `/lib/firmare/iwlwifi-9260*`. If the files doesn't exist, download at the ling below and move to the specified previous location
  ```
  git clone git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git
  sudo cp linux-firmware/iwlwifi-9260* /lib/firmware/
  ```
  
  Source: https://forums.developer.nvidia.com/t/intel-ac9260-wifi-card-stops-working-after-upgrade-to-jetpack-4-5/167892

* To Enable Bluetooth
```
git clone https://github.com/yoffy/jetson-nano-kernel.git
./download-kernel.sh
./install-btusb.sh
```

Source: https://github.com/yoffy/jetson-nano-kernel
