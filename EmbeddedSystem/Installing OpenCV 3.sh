#!/bin/sh

#Installing OpenCV 3 on a Raspberry Pi 3 running Raspbian Jessie
###################
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update
sudo reboot
###################
sudo apt-get install build-essential git cmake pkg-config
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk2.0-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python2.7-dev python3-dev
sudo apt-get install python-numpy
###################
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
unzip opencv.zip
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
cd ~/opencv-3.1.0/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D INSTALL_C_EXAMPLES=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv-3.1.0/modules \
-D BUILD_EXAMPLES=ON ..
make clean
make -j4
sudo make install
sudo ldconfig
