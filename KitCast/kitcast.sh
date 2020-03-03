#!/usr/bin/bash


if [ $# -lt 3 ];
    then
        python3 ~/.KitCast/KitCast/app.py $1 $2
    elif[ s# -lt 5 ];
    then
        python3 ~/.KitCast/KitCast/app.py $1 $2 $3 $4
    else
        python3 ~/.KitCast/KitCast/app.py $1 $2 $3 $4 $5 $6
fi

