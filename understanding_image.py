import cv2

img = cv2.imread('/home/karuna/Pictures/dog.jpg')
# accessing pixel value at a particular coordinate
px = img[100,100]
print(px)

# finding image height , width and number of channels
print(img.shape)

# finding the datatype of the image
print(img.dtype)
cv2.imshow('Win',img)
cv2.waitKey(0)