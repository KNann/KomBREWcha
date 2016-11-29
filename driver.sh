#! /bin/bash

#### Purpose #####
#This code runs all of the necessary scripts for the KomBREWcha brewing
#monitor

#################

#ensure we are in the correct directory
cd ~
cd KomBREWcha

./img_capture.sh #take and resize the pictures
./visColors.py #analyze the levels of red and green light in each picture

#read the last line output from colorAnalyze (determines maturity and graphs progress)
#the last line is a 1 or 0 indicating the brews readiness
#1 indicates brew is ready
#0 indicates brew is not ready
var=`./colorAnalyze.py | tail -1`

#write to a text file to be read by the user interface
echo $var > complete.txt


