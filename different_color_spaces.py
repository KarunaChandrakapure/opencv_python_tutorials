import cv2

# Load input image in BGR format (default in OpenCV)
img = cv2.imread('dog.jpg')

# Convert BGR to Grayscale — reduces to single intensity channel
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert BGR to HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display image
cv2.imshow('Win', img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
