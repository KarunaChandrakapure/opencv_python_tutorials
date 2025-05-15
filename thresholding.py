import cv2

img = cv2.imread('apple.jpeg',0)

# THRESH_BINARY: If pixel > 127 -> 255 else 0
ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# THRESH_BINARY_INV: Inverted binary threshold
ret2, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# THRESH_TRUNC: If pixel > 127 -> 127 else unchanged
ret3, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

# THRESH_TOZERO: If pixel < 127 -> 0 else unchanged
ret4, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

# THRESH_TOZERO_INV: If pixel > 127 -> 0 else unchanged
ret5, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


### Otsu's Thresholding (automatic threshold estimation) ###
# Apply Gaussian Blur first to reduce noise
blur = cv2.GaussianBlur(img, (5, 5), 0)
# THRESH_BINARY + THRESH_OTSU automatically finds optimal threshold
ret6, thresh6 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


### Adaptive Thresholding Techniques ###
# ADAPTIVE_THRESH_MEAN_C: Threshold is mean of neighborhood minus C
thresh7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 11, 2)

# ADAPTIVE_THRESH_GAUSSIAN_C: Threshold is weighted sum (Gaussian) of neighborhood minus C
thresh8 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 2)


hcont_img = cv2.hconcat([img,thresh1,thresh2,thresh3,thresh4,thresh5,thresh6,thresh7,thresh8])
cv2.imshow('Win',hcont_img)
cv2.waitKey(0)
cv2.destroyAllWindows()