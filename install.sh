#!/bin/bash

echo "v8"
sudo npm install castnow -g #instala as dependencias
mkdir ~/.KitCast #cria um diretorio na home
sudo cp KitCast/* ~/.KitCast #copia pra esse diretorio
sudo cp /KitCast/kitcast.sh /usr/local/bin/kitcast #copia o script executavel pra bin
chmod +x /KitCast/app.py
echo "succesfully installed"


