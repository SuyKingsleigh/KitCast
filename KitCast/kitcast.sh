#!/usr/bin/bash


if [ $# -lt 3 ];
    then
        python3 ~/.KitCast/KitCast/app.py $1 $2
    else
        python3 ~/.KitCast/KitCast/app.py $1 $2 $3 $4
fi

