# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import os.path
import numpy as np 
directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'hbay.jpg')
img = plt.imread(filename)  
height = len(img)
width = len(img[0])
for row in range(0, 250):
    for column in range(0, 1920):
        img[row][column] = [255, 255, 0] 
height = len(img)
width = len(img[0])
for row in range(1670, 1920):
    for column in range(0, 1920):
        img[row][column] = [255, 255, 0]
height = len(img)
width = len(img[0])
for row in range(500, 900):
    for column in range(200, 500):
        img[row][column] = [160, 224, 0] 
height = len(img)
width = len(img[0])
for row in range(500, 900):
    for column in range(1400, 1700):
        img[row][column] = [160, 224, 0]  
height = len(img)
width = len(img[0])
for row in range(1300, 1400):
    for column in range(500, 1350):
        img[row][column] = [255, 0, 0] 
height = len(img)
width = len(img[0])
for row in range(650, 750):
    for column in range(325, 375):
        img[row][column] = [51, 153, 255] 
height = len(img)
width = len(img[0])
for row in range(650, 750):
    for column in range(1525, 1575):
        img[row][column] = [51, 153, 255] 
height = len(img)
width = len(img[0])
for r in range(250,499):
    for c in range(width):
        if sum(img[r][c])>300:
            img[r][c]=[255,0,255] 
height = len(img)
width = len(img[0])
for r in range(1400,1650):
    for c in range(width):
        if sum(img[r][c])<300: 
            img[r][c]=[229,204,255] 
fig, ax = plt.subplots(1, 1)
ax.imshow(img, interpolation='none')
fig.show()
