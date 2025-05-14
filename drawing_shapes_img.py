import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a line
# argument : (img , start_coordinates , end_coordinates , color , thickness)
cv2.line(img, (100, 100), (100, 200), (255, 255, 255), 5)

# Draw a circle
# argument : (img, center_coordinate , radius , color , thickness)
cv2.circle(img, (400, 400), 25, (0, 255, 255), 3)

# Draw a rectangle
# argument : (img, top_left , bottom_right , color , thickness)
cv2.rectangle(img, (180, 250), (280, 450), (0, 0, 255), 3)

# Draw a polygon
# argument : (img , coordinates , closed/open , color)
pts = np.array([[100, 50], [50, 30], [80, 20], [50, 100]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (255, 0, 0))

# Write Text
# argument : (img,text,coordinates,Font type,Font scale,color,thickness)
cv2.putText(img, 'Hello World', (190, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0), 1)

cv2.imshow('Win', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
