import cv2
import os

# argument 0 is given to use the default camera
camera = cv2.VideoCapture(0)
# Check if the camera object is created successfully
if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()