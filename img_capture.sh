#! /bin/bash

###### Purpose ########
#This code takes a picture of the kombucha brew and resizes it for faster
#processing by visColors.py

######################
cd ~
cd KomBREWcha

raspistill -v -vf -hf -o "kombucha.jpg"

convert kombucha.jpg -resize 328x246 kombuchasmall.jpg
