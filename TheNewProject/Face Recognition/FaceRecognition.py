import cv2
import os
import pickle
import threading

cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
count = 0
pathcount = 0
labels = {}

with open("labels.txt", 'rb') as f:
    _labels = pickle.load(f)
    labels = {v:k for k,v in _labels.items()}


video_capture = cv2.VideoCapture(0)

class timerTimer:
    timer = 1

    def timerTimer2(self):
        timerTimer.timer = 0
        print("lol")
timerTimer = timerTimer()
timerTimer.timer = 0


while True:
    # Capture frame-by-frame
    ret, frames = video_capture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=7,
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_colour = frames[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roi_gray)

        print(conf)

        if conf >= 0 and conf <= 70:
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frames, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

        elif conf >= 65 and conf <=100:
            #unknown face
            font = cv2.FONT_HERSHEY_SIMPLEX
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frames, "unknown", (x, y), font, 1, color, stroke, cv2.LINE_AA)

            if timerTimer.timer == 0:
                print("Entered")
                while True:
                    path = os.path.join(r"C:\\Users\\delay\\PycharmProjects\\pythonProject\\TheNewProject\\Face Recognition\\ToProcess\\", str(pathcount))

                    if os.path.exists(path):
                        print("path exists")
                        pathcount = pathcount + 1

                    else:
                        print("Unknown Face, Writing")
                        os.mkdir(path)
                        for x in range(10):
                            cv2.imwrite(os.path.join(path, 'face' + str(count)+ '.jpg'), roi_colour)
                            count = count + 1

                        threading.Timer(10, timerTimer.timerTimer2).start()
                        timerTimer.timer = 1
                        break


            else:
                print("cooldown")



        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
