#!/usr/bin/python

import datetime
import time
import matplotlib.pyplot as plt

time = []
Rval = []
Gval = []
Bval = []

f = open('colorsLog.txt')

line = f.readline()

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

Rthresh = 60
Gthresh = 85
if Rlast < Rthresh:
    complete = 1
    
elif Glast > Gthresh:
    complete = 1

##print complete

#reads the most recent line in the file
# by | delimiters:
### first column: date stamp
### second column: R value
### third column: G value
### fourth column: B value



# ( )   Plot the graph!
# fig = plt.figure()
# ax = p3.Axes3D(fig)
# ax.scatter(h_, v_, i, s=5, c=colours, lw=0)
# ax.set_xlabel('Hue')
# ax.set_ylabel('Value')
# ax.set_zlabel('Intensity')
# fig.add_axes(ax)
# plt.show()

