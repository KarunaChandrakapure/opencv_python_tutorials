import cv2
path = '/home/karuna/AssertAI_Projects/AF_OCR/output.mp4'
# create a video capture object and pass vid path as argument , (0 for webcam)
vid = cv2.VideoCapture(path)

# Define the codec and create VideoWriter object (vid name , codec, fps,(width,height))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,  480))

while True:
    # read video frame by frame ,
    # returns img and a bool val (True if image is read correctly else false)
    ret, img = vid.read()
    if ret :
        #process your frame / perform your task
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # display image
        cv2.imshow('Win',gray_img)

        #write the gray frame
        out.write(gray_img)
    else:
        print('Error in reading video, Please check the path or video format')
        exit()
    # if ESC is pressed end the video
    if cv2.waitKey(1)==27:
        break

# release the capture and destroy all windows
vid.release()
cv2.destroyAllWindows()