#!/usr/bin/python

file = open('colorsLog.txt','r')

#reads the most recent line in the file
# by | delimiters:
### first column: date stamp
### second column: R value
### third column: G value
### fourth column: B value
print file.readline()

# ( )   Plot the graph!
# fig = plt.figure()
# ax = p3.Axes3D(fig)
# ax.scatter(h_, v_, i, s=5, c=colours, lw=0)
# ax.set_xlabel('Hue')
# ax.set_ylabel('Value')
# ax.set_zlabel('Intensity')
# fig.add_axes(ax)
# plt.show()

