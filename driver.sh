#! /bin/bash

#### Purpose #####
#This code runs all of the necessary scripts for the KomBREWcha brewing
#monitor

#################

cd ~
cd KomBREWcha

./img_capture.sh
./visColors.py
var=`./colorAnalyze.py | tail -1`
#echo $var

if [ $var==1 ]
then
    echo "complete"
else
    echo "not ready"
fi

