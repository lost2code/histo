#Learn how values (pixel (bgr) intensities) are distributed in a color image

from matplotlib import pyplot as plt
import cv2


#1) loading an image (in color)
mem_image = cv2.imread('d:/images/work.png', cv2.IMREAD_COLOR)

mem_image = cv2.resize(mem_image, (1200,800))
print(mem_image.shape)

#2) render the image
cv2.imshow('IMG', mem_image)

#3) hist(data, bins, range)
col = ['b', 'g','r'] # blue, green and red
for i in range(3):  #i=0 (blue), i=1(green), i =2 (red)
    i_channel_histogram = cv2.calcHist(images = [mem_image], channels = [i], mask=None, histSize=[256], ranges=[0,255])
    plt.plot(i_channel_histogram, color = col[i])

plt.show()

#FYI
#A histogram is a representation of distribution of values of a dataset.

#2D numpy array can be converted into a 1D array using flatten()