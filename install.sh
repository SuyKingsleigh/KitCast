#!/bin/bash

sudo npm install castnow -g
mkdir ~/.KitCast
sudo cp -r KitCast ~/.KitCast
sudo cp -r ~/.KitCast/KitCast/kitcast.sh /usr/local/bin/kitcast
chmod +x ~/.KitCast/KitCast/app.py
echo "succesfully installed"


