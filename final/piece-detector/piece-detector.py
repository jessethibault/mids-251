import cv2
import time

# Initiate video capture
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resize to image size indentifier is expecting (and save tons of space)
    dim = (128, 128)
    resized = cv2.resize(frame, dim)

    # Save image to disc for identifier
    cv2.imwrite(f'/final/images/{round(time.time() * 1000000)}.jpg', resized)

    # Only update every quarter second
    time.sleep(0.25)