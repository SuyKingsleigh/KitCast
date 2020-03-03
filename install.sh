#!/bin/bash

check_dir_files(){
    if [[ -d "~/.KitCast" ]]
        then
        sudo rm -rf ~/.KitCast
        echo "reinstalling"
    fi

    if [[ -f "/usr/local/bin/kitcast" ]]
    then
        sudo rm -f /usr/local/bin/kitcast
    fi
}

check_dir_files
if which castnow > /dev/null; then
    echo "Castnow already installed"
else
    echo "Installing dependencies"
    sudo npm install castnow -g
fi
sudo rm -rf ~/.KitCast
mkdir ~/.KitCast

sudo cp -r KitCast ~/.KitCast
sudo cp -r ~/.KitCast/KitCast/kitcast.sh /usr/local/bin/kitcast


