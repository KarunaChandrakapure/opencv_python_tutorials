import cv2
import numpy as np

img = cv2.imread('apple.jpeg')

# resizing any image
print(img.shape)
# res = cv2.resize(img,(1000,800))
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
print(res.shape)

# cv2.ROTATE_90_CLOCKWISE
# cv2.ROTATE_90_COUNTERCLOCKWISE
# cv2.ROTATE_180
rotated = cv2.rotate(res, cv2.ROTATE_90_CLOCKWISE)

# 0 : Flip vertically
# 1 : Flip horizontally
# -1 : Flip both vertically and horizontally
flip_horizontal = cv2.flip(img, -1)

# Read image
img = cv2.imread('img1.jpeg')
rows, cols, ch = img.shape

### Affine Transform ###
# Source points (3 points)
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
# Destination points (3 points)
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Get Affine Transform Matrix
M_affine = cv2.getAffineTransform(pts1, pts2)

# Apply Affine Transform
dst_affine = cv2.warpAffine(img, M_affine, (cols, rows))


### Perspective Transform ###
# Source points (4 points)
pts1_p = np.float32([[56,65], [368,52], [28,387], [389,390]])
# Destination points (4 points)
pts2_p = np.float32([[0,0], [300,0], [0,300], [300,300]])

# Get Perspective Transform Matrix
M_perspective = cv2.getPerspectiveTransform(pts1_p, pts2_p)

# Apply Perspective Transform
dst_perspective = cv2.warpPerspective(img, M_perspective, (300, 300))


cv2.imshow('Original Image', img)
cv2.imshow('Affine Transform', dst_affine)
cv2.imshow('Perspective Transform', dst_perspective)

cv2.waitKey(0)
cv2.destroyAllWindows()


