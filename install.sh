#!/bin/bash

sudo npm install castnow -g #instala as dependencias
mkdir ~/.KitCast #cria um diretorio na home
sudo cp -r KitCast ~/.KitCast #copia pra esse diretorio
sudo cp -r ~/.KitCast/KitCast/kitcast.sh /usr/local/bin/kitcast #copia o script executavel pra bin
chmod +x ~/.KitCast/KitCast/app.py
echo "succesfully installed"


