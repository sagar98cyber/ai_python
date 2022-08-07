import cv2
import numpy as np

image = cv2.imread('E:/MD/flower.jpg')

cv2.imshow('flower',image)


cv2.destroyWindow('flower')


cv2.imwrite('E:/MD/flower.png',image)


image = cv2.imread('E:/MD/dolphin.jpg')

image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('dolphin',image)


cv2.imwrite('edges_dolphin.jpg',cv2.Canny(image,200,300))


cv2.imshow('edges', cv2.imread('edges_dolphin.jpg'))

