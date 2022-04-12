#Learn how values (pixel intensities) are distributed in a grayscale image

from matplotlib import pyplot as plt
import cv2
import numpy as np


#1) make an image
#mem_image = np.zeros((300,300), dtype=np.uint8)
#lets add a vertical gray band
#mem_image[:,100:200] = 127 #arr[allrows, cols 100 to 199] = 127 i.e. gray
#lets add a vertical white band
#mem_image[:,200:300] = 255 #arr[allrows, cols 200 to 299] = 255 i.e. white

#or
#1) loading an image (in grayscale)
mem_image = cv2.imread('d:/images/kids.jpg', cv2.IMREAD_GRAYSCALE)
mem_image = cv2.resize(mem_image, (1200,800))
#print(mem_image.shape)

#2) render the image
cv2.imshow('IMG', mem_image)

#3) hist(data, bins, range)
plt.hist(x = mem_image.flatten(), bins = 256, range = (0,255))

plt.show()

#FYI
#A histogram is a representation of distribution of values of a dataset.

#2D numpy array can be converted into a 1D array using flatten()