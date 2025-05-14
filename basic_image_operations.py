import cv2

# imread : read image from folder
# cv2.IMREAD_COLOR : loads the image in the BGR 8-bit format
# cv2.IMREAD_GRAYSCALE : loads image in grayscale format
# cv2.IMREAD_UNCHANGED : loads the image including alpha channel
img = cv2.imread('/home/karuna/Pictures/dog.jpg',cv2.IMREAD_GRAYSCALE)

#cv2.imshow : function to display image
cv2.imshow('Win',img)

# cv2.waitKey : function to display a window for given milliseconds or until any key is pressed.
# It takes time in milliseconds as a parameter and waits for the given time to destroy the window

#cv2.imwrite : function to save image 
if cv2.waitKey(0) == ord('s'):
    cv2.imwrite('dog.png',img)

