#!/usr/bin/python

import datetime
import time

time = []
Rval = []
Gval = []
Bval = []

f = open('colorsLog.txt')

line = f.readline()

tstart = line.split("|")[0]

#create time and RBG value vectors from colorsLog.txt
while line:
    tstr = line.split("|")[1]
    t = float(tstr)/(3600*24)
    time.append(t)
    Rstr = line.split("|")[2]
    R = float(Rstr)
    Rval.append(R)
    Gstr = line.split("|")[3]
    G = float(Gstr)
    Gval.append(G)
    Bstr = line.split("|")[4]
    B = float(Bstr)
    Bval.append(B)
    line = f.readline()
f.close()

#convert timestamp data to time since start of batch
t0 = time[0]
i=0
while i<len(time):
    time[i] = time[i]-t0
    i = i+1

print time
print Rval
print Gval

Rlast = Rval[-1]
Glast = Gval[-1]
##print Rlast
##print Glast

complete = 0

#Rthresh = 60
#Gthresh = 85
if Rlast < Glast:
    complete = 1

##print complete

##Graph Results
import numpy as np
import pylab as pl

pl.plot(time, Rval, 'r')
pl.plot(time, Gval, 'g')

# Format graph
FileName = 'Batch Started: '+tstart
pl.title('Batch Progress')
pl.xlabel('time (days)')
pl.ylabel('R and G levels')

# save graph image in specific folder
import os
fld = '/home/pi/KomBREWcha/Batch_Progress_Graphs'
if not os.path.isdir(fld): os.makedirs(fld)
pl.savefig(os.path.join(fld, FileName))
# pl.show()


