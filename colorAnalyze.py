#!/usr/bin/python

time = []
Rval = []
Gval = []
Bval = []

f = open('colorsLog.txt')

line = f.readline()

t = line.split("|")[0]
R = line.split("|")[1]
G = line.split("|")[2]
B = line.split("|")[3]
print t
print R
print G
print B

##while line:
##    print line
##    line = f.readline()
##f.close()
##print data 

#reads the most recent line in the file
# by | delimiters:
### first column: date stamp
### second column: R value
### third column: G value
### fourth column: B value


##recent = file.readline()
##print recent
##
##print ""
##
##vars = recent.split("|")
##print vars


# ( )   Plot the graph!
# fig = plt.figure()
# ax = p3.Axes3D(fig)
# ax.scatter(h_, v_, i, s=5, c=colours, lw=0)
# ax.set_xlabel('Hue')
# ax.set_ylabel('Value')
# ax.set_zlabel('Intensity')
# fig.add_axes(ax)
# plt.show()

