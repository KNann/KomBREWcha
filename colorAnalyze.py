#!/usr/bin/python

import datetime
import time

#initialize vectors to graph from later
time = []
Rval = []
Gval = []
Bval = []

#read colorsLog.txt line by line and parse each line by the | character
f = open('colorsLog.txt')

line = f.readline()

#time stamp is the first field of the first line of the file
tstart = line.split("|")[0]

#create time and RBG value vectors from colorsLog.txt
while line:
    #the second field is time represented in seconds, convert to days and add to time vector
    tstr = line.split("|")[1]
    t = float(tstr)/(3600*24)
    time.append(t)
    
    #the next field is the level of red light in the images
    Rstr = line.split("|")[2]
    R = float(Rstr)
    Rval.append(R)

    #level of green light in the images
    Gstr = line.split("|")[3]
    G = float(Gstr)
    Gval.append(G)

    #level of blue light in the images
    Bstr = line.split("|")[4]
    B = float(Bstr)
    Bval.append(B)

    #read the next line
    line = f.readline()
f.close()

#convert timestamp data to time since start of batch
t0 = time[0]
i=0

#for each value in the time vector subtract the start time
while i<len(time):
    time[i] = time[i]-t0
    i = i+1

##debugging purposes
print time
print Rval
print Gval

#look at the most recent levels of red and green light 
Rlast = Rval[-1]
Glast = Gval[-1]
#print Rlast
#print Glast

#assume brew is not ready
complete = 0

##what determines readiness may be threshold values or the values in relation to one another
##currently the test is if green light is greater than red light, further tests are needed
#Rthresh = 60
#Gthresh = 85
if Rlast < Glast:
    complete = 1

#the driver code will read this value and give user feedback whether or not the brew is complete
print complete

##Graph Results
import numpy as np
import pylab as pl

#red levels are represented by a red line, green levels by a green line
##groundbreaking stuff
pl.plot(time, Rval, 'r')
pl.plot(time, Gval, 'g')

# Format graph
FileName = 'Batch Started: '+tstart
pl.title('Batch Progress')
pl.xlabel('time (days)')
pl.ylabel('R and G levels')

# save graph image in specific folder if hte folder doesn't exist, make it
import os
fld = '/home/pi/KomBREWcha/Batch_Progress_Graphs'
if not os.path.isdir(fld): os.makedirs(fld)
pl.savefig(os.path.join(fld, FileName))
# pl.show()


