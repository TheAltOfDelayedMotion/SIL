######################################################
#FACE DETECTION LIBRARY (Module for training AI model)
#Usage
#dsf60(60, 0)
#call dsf60(a, b)
#a = amount of faces to be captured
#b = starting count (keep at zero)
######################################################

import cv2
import os


filename = 'face_1.jpg'
path = r"C:\Users\delay\PycharmProjects\pythonProject\TheNewProject\Face Recognition\ToProcess"
cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

def dsf60(amount, count):
    while True:
        # Capture frame-by-frame
        ret, frames = video_capture.read()
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # Draw a rectangle around the faces

        for (x, y, w, h) in faces:
            cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi_color = frames[y:y + h, x:x + w]

            if count < (amount + 1):
                cv2.imwrite(os.path.join(path, str(count) + '.jpg') , roi_color)
                count = count + 1

            else:
                video_capture.release()
                cv2.destroyAllWindows()


        #Display the resulting frame
        cv2.imshow('Video', frames)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            video_capture.release()
            video_capture.release()

dsf60(80, 0)



