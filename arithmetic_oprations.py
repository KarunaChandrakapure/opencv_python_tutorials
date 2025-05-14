import cv2

# Read and resize the first image
img1 = cv2.imread('dog.jpg')
img1 = cv2.resize(img1, (224, 224))

# Read and resize the second image (logo)
img2 = cv2.imread('logo.png')
img2 = cv2.resize(img2, (224, 224))

# Add the two images pixel-wise (saturated addition)
img3 = cv2.add(img2, img1)  # Each pixel: img3 = img1 + img2 (values capped at 255)

# Blend the two images with specific weights (alpha blending)
img4 = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)  # img4 = 0.7*img1 + 0.3*img2

# Subtract the first image from the second (pixel-wise)
img5 = cv2.subtract(img2, img1)  # Each pixel: img5 = img2 - img1 (no negative values; underflow clipped to 0)

# Invert the first image (bitwise NOT)
img6 = cv2.bitwise_not(img1)  # Inverts each bit of every pixel in img1

# Convert the first image to grayscale
img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # Convert BGR image to grayscale

# Apply a binary threshold to create a mask
ret, mask = cv2.threshold(img2gray, 100, 200, cv2.THRESH_BINARY)
# If pixel > 100 → set to 200, else → set to 0

# Apply the mask to img1 using bitwise AND
img7 = cv2.bitwise_and(img1, img1, mask=mask)
# Keeps only the parts of img1 where the mask is non-zero

# Display the final image
cv2.imshow('Win', img7)
cv2.waitKey(0)
cv2.destroyAllWindows()
