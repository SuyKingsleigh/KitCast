#!/usr/bin/bash

app="~/.KitCast/KitCast/app.py"
if [ $# -lt 3 ];
    then
        ./$app $1 $2
    else
        ./$app $1 $2 $3 $4
fi

