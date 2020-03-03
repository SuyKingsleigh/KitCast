#!/usr/bin/bash

app="~/.KitCast/KitCast/app.py"
#app="coiso.py"
if [ $# -lt 3 ];
    then
        python3 $app $1 $2
    else
        python3 $app $1 $2 $3 $4
fi

