# This is a simple application to get the coordinates wherever we double-click on it
# and draw polygon/roi using it

import numpy as np
import cv2

coordinates = []

# Mouse callback function
def get_coord(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(param, (x, y), 5, (255, 0, 0), -1)
        coordinates.append([x, y])

def main():
    # Create a black image
    img = np.zeros((512, 512, 3), np.uint8)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', get_coord, img)

    while True:
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == 27:  # ESC key to break
            break

    # Draw polygon if at least 3 points were selected
    if len(coordinates) >= 3:
        pts = np.array(coordinates, np.int32).reshape((-1, 1, 2))
        cv2.polylines(img, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

    cv2.imshow('Polygon ROI', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
