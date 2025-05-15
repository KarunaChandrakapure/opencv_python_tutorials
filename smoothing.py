import cv2


img = cv2.imread('apple.jpeg')

# 1. Normal Averaging Blur (box blur)
# Each pixel is replaced by the average of its neighbors within the 5x5 kernel
blur1 = cv2.blur(img, (5, 5))

# 2. Gaussian Blur
# Weighted average using a Gaussian kernel, reduces noise and detail
blur2 = cv2.GaussianBlur(img, (5, 5), 0)

# 3. Median Blur
# Each pixel is replaced by the median of its neighbors, effective for salt-and-pepper noise
blur3 = cv2.medianBlur(img, 5)

# 4. Bilateral Filter
# Smooths while keeping edges sharp; preserves edges by combining domain and range filtering
blur4 = cv2.bilateralFilter(img, 9, 75, 75)



vcont_img = cv2.vconcat([img, blur1, blur2, blur3, blur4])
cv2.imshow('Win', vcont_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
