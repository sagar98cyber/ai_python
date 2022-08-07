import cv2
import numpy as np

image = cv2.imread("flower.jpg")

image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('flower',image)
cv2.waitKey(0)

cv2.imwrite('edges_flower.jpg',cv2.Canny(image,200,300))
#cv2.destroyWindow('flower.jpg')

cv2.imwrite("flower.png",image)
cv2.imshow('flower',image)
image = cv2.imread("dolphin.jpg")

image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('dolphin',image)
cv2.waitKey(0)

cv2.imwrite('edges_dolphin.jpg',cv2.Canny(image,200,300))

cv2.imshow('edges', cv2.imread('edges_dolphin.jpg'))
cv2.waitKey(0)