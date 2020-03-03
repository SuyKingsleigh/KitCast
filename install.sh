#!/bin/bash

echo "v3"
sudo npm install castnow -g
chmod +x kitcast.py
sudo cp KitCast /usr/local/bin/KitCast
sudo cp kitcast.sh /usr/local/bin/kitcast
echo "succesfully installed"


