#!/usr/bin/python
#original file from MarkSolters/rainbow-vision on github.com

import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import colorsys
from PIL import Image

# (1) Import the file to be analyzed!
img_file = Image.open("small.jpg")
img = img_file.load()

# (2) Construct a blank matrix representing the pixels in the image
[xs, ys] = img_file.size
max_intensity = 100
hues = {}

# (3) Examine each pixel in the image file
for x in xrange(0, xs):
  for y in xrange(0, ys):
    # ( )  Get the RGB color of the pixel
    [r, g, b] = img[x, y]

    # ( )  Normalize pixel color values
    # r /= 255.0
    # g /= 255.0
    # b /= 255.0

    # ( )  Convert RGB color to HSV
    [h, s, v] = colorsys.rgb_to_hsv(r, g, b)
    if h not in hues:
      hues[h] = {}
      if v not in hues[h]:
        hues[h][v] = 1
      else:
        if hues[h][v] < max_intensity:
          hues[h][v] += 1

# print(hues)
# ( )   Decompose the hues tree into a set of dimensional arrays we can use with matplotlib
h_ = []
v_ = []
i = []
colours = []

for h in hues:
  for v in hues[h]:
    h_.append(h)
    v_.append(v)
    i.append(hues[h][v])
    [r, g, b] = colorsys.hsv_to_rgb(h, 1, v)
    colours.append([r, g, b])

#NOT FROM SOURCE CODE

colorCeiling = len(colours)

# you can modify these value for whatever given range that you want 
colorMin = colorCeiling / 3
colorMax = 2 * colorCeiling / 3 
colorRange = colorMax - colorMin

avgR = 0 
avgG = 0
avgB = 0

# sum of RGB values for a specified range
for i in range(colorCeiling):
  if colorMin <= i <= colorMax:
    avgR += colours[i][0]
    avgG += colours[i][1]
    avgB += colours[i][2]


#find the average RGB value for a given section and write it to your input file
if (colorRange != 0) :
  avgRGB = [avgR / colorRange, avgG / colorRange, avgB / colorRange]
else:
  avgRGB = colours[0]
#RGBString = '[' + str(avgRGB[0]) + ', ' + str(avgRGB[1]) + ', ' + str(avgRGB[2]) + ']'
RGBString = '|'+str(avgRGB[0])+'|'+str(avgRGB[1])+'|'+str(avgRGB[2])+'\r'


# Append to input file
import datetime
time = '['+str(datetime.datetime.now())+'] '
# f = open('file', 'w')
# f.write(RGBString)
with open("colorsLog.txt", "a") as myfile:
  myfile.write(time)
  myfile.write(RGBString)



# ( )   Plot the graph!
# fig = plt.figure()p;l
# ax = p3.Axes3D(fig)
# ax.scatter(h_, v_, i, s=5, c=colours, lw=0)
# ax.set_xlabel('Hue')
# ax.set_ylabel('Value')
# ax.set_zlabel('Intensity')
# fig.add_axes(ax)
# plt.show()
