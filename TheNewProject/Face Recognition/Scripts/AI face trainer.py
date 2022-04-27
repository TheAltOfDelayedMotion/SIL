import os
import pickle
import Directory
from PIL import Image
import numpy as np
import cv2

#fileread = open()
labelstxt = os.path.join(Directory.datadir, "labels.txt")
trainneryml = os.path.join(Directory.datadir, "trainner.yml")

def facetrainer():
    face_cascade = cv2.CascadeClassifier(os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    image_dir = r"C:\Users\delay\PycharmProjects\pythonProject\TheNewProject\Face Recognition\TrainedFaces\1"

    current_id = 0

    label_ids = {}

    y_labels = []
    x_train = []

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(Directory.timgdir, "1",  file)
                label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()

                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1

                id_ = label_ids[label]

                pil_image = Image.open(path).convert("L")
                image_array = np.array(pil_image, 'uint8')

                faces = face_cascade.detectMultiScale(image_array,

                                                      scaleFactor=1.1,
                                                      minNeighbors=5)

                for (x,y,w,h) in faces:
                    roi = image_array[y:y+h, x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)

    with open(labelstxt, 'wb') as f:
        pickle.dump(label_ids, f)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save(trainneryml)

facetrainer()
