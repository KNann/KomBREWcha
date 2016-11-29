#! /bin/bash

###### Purpose #######
#This code resets files to record data for a new kombucha batch

######
cd ~
cd KomBREWcha

#delete colorsLog text file, all analysis is run from this file and graphs are titled
#from the first line of this file
##by deleting the text file, the code that writes to it will create a new one and a new graph will be made
rm colorsLog.txt

#run the normal procedure code
./driver.sh
