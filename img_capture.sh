#! /bin/bash

###### Purpose ########
#This code takes a picture of the kombucha brew and resizes it for faster
#processing by visColors.py

######################
cd ~
cd KomBREWcha

raspistill -v -vf -hf -o "kombucha1.jpg"
raspistill -v -vf -hf -o "kombucha2.jpg"
raspistill -v -vf -hf -o "kombucha3.jpg"

convert kombucha1.jpg -resize 328x246 kombuchasmall1.jpg
convert kombucha2.jpg -resize 328x246 kombuchasmall2.jpg
convert kombucha3.jpg -resize 328x246 kombuchasmall3.jpg
