#!/usr/bin/python

time = []
Rval = []
Gval = []
Bval = []

f = open('colorsLog.txt')

line = f.readline()

while line:
    #print line
##    t = line.split("|")[0]
##    
##    time.append(t)
    Rstr = line.split("|")[1]
    R = float(Rstr)
    Rval.append(R)
    Gstr = line.split("|")[2]
    G = float(Gstr)
    Gval.append(G)
    Bstr = line.split("|")[3]
    B = float(Bstr)
    Bval.append(B)
    line = f.readline()
f.close()
 
print time
print Rval
print Gval

Rlast = Rval[-1]
Glast = Gval[-1]
print Rlast
print Glast

complete = 0

Rthresh = 60
Gthresh = 75
if Rlast < Rthresh:
    complete = 1
elif Glast > Gthresh:
    complete = 1

print complete

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

