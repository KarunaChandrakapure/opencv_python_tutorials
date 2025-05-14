# This python code is to create a trackbars to specify each of BGR colors

import cv2
import numpy as np

# Dummy callback function required by createTrackbar
def nothing(x):
    pass

# Create a black image of size 512x512 pixels with 3 color channels (BGR)
img = np.zeros((512, 512, 3), np.uint8)

# Create a window named 'Win'
cv2.namedWindow('Win')

# Create 3 trackbars (sliders) for Red, Green, and Blue channels in the window 'Win'
# These let the user control the color interactively
cv2.createTrackbar('R', 'Win', 0, 255, nothing)  # Red channel
cv2.createTrackbar('G', 'Win', 0, 255, nothing)  # Green channel
cv2.createTrackbar('B', 'Win', 0, 255, nothing)  # Blue channel

while True:
    # Display the image in the window
    cv2.imshow('Win', img)

    # If ESC key is pressed, break the loop
    if cv2.waitKey(1) == 27:
        break

    # Get the current positions of the R, G, B trackbars
    r = cv2.getTrackbarPos('R', 'Win')
    g = cv2.getTrackbarPos('G', 'Win')
    b = cv2.getTrackbarPos('B', 'Win')

    # Update the image color to the selected BGR values
    img[:] = [b, g, r]

cv2.destroyAllWindows()
