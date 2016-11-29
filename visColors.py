#!/usr/bin/python
#original file from MarkSolters/rainbow-vision on github.com

import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import colorsys
from PIL import Image

# (1) Import the files to be analyzed!
##we noticed the readings were inconsistent between images of the same batch
##but were more consistent when averaged between three images
img_file1 = Image.open("kombuchasmall1.jpg")
img1 = img_file1.load()

img_file2 = Image.open("kombuchasmall2.jpg")
img2 = img_file2.load()

img_file3 = Image.open("kombuchasmall3.jpg")
img3 = img_file3.load()

img_list = [img1, img2, img3]
trial_avg = [0, 0, 0]
##the process for one image is from open source code and edited to accomodate three images
# (2) Construct a blank matrix representing the pixels in the image
for img in img_list:
  [xs, ys] = img_file1.size #all images are the same size
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
##right not we are taking the middle third of the image
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

#store the total RGB averages as 1/3 of the average for each of the three images
  trial_avg[0] = trial_avg[0] + avgRGB[0]/3
  trial_avg[1] = trial_avg[1] + avgRGB[1]/3
  trial_avg[2] = trial_avg[2] + avgRGB[2]/3

Rstr = "%.3f" % trial_avg[0]
Gstr = "%.3f" % trial_avg[1]
Bstr = "%.3f" % trial_avg[2]
#RGBString = '|'+str(trial_avg[0])+'|'+str(trial_avg[1])+'|'+str(trial_avg[2])+'\n'
RGBString = '|'+Rstr+'|'+Gstr+'|'+Bstr+'\n'


# Append to input file
import datetime
import time

#get the current time without microseconds
t = datetime.datetime.now().replace(microsecond=0)
dt = str(t) #string of M-D-Y time format
t1 = t.timetuple()
dec_time = time.mktime(t1)
batchtime = str(dec_time) #time as a number of seconds for graphing purposes
timeString = dt+'|'+batchtime
##time_tuple = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
##print(time_tuple)

#write the time stamp, graphable time, and  RGB values to colorsLog.txt
with open("colorsLog.txt", "a") as myfile:
  myfile.write(timeString)
  myfile.write(RGBString)


