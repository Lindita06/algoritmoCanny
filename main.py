import pydicom
import cv2
import numpy as np
from matplotlib import pyplot as plt

img_dicom = pydicom.dcmread('0004.DCM')
img = img_dicom.pixel_array

edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
