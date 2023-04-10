# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import cv2
import numpy as np

# Read the input image
img = cv2.imread('image1.jpg')

# Resize the image
img = cv2.resize(img, (960, 540))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median blur to remove noise
gray = cv2.medianBlur(gray, 5)

# Apply adaptive thresholding to detect edges
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Apply bilateral filter to smooth out colors while preserving edges
color = cv2.bilateralFilter(img, 9, 300, 300)

# Create a blank image with the same size as the input image
cartoon = np.zeros_like(img)

# Loop over each channel in the color image and apply the edges mask
for i in range(3):
    cartoon[:,:,i] = cv2.bitwise_and(color[:,:,i], color[:,:,i], mask=edges)

# Display the output image
cv2.imshow('Cartoonized Image', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
