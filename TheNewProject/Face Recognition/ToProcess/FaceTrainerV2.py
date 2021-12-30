import os
import pickle
from PIL import Image
import numpy as np
import cv2

with open("../labels.txt", 'rb') as f:
    _labels = pickle.load(f)
    labels = {v:k for k,v in _labels.items()}

def facetrainer():
    face_cascade = cv2.CascadeClassifier(os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(r"C:\Users\delay\PycharmProjects\pythonProject\TheNewProject\Face Recognition\trainner.yml")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, "../../Faces")

    current_id = 0

    label_ids = {}

    y_labels = []
    x_train = []

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
                print("Picture Found")

                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1

                id_ = label_ids[label]

                pil_image = Image.open(path).convert("L")
                image_array = np.array(pil_image, 'uint8')

                picture = cv2.imread(path)
                gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(image_array,
                                                      scaleFactor=1.1,
                                                      minNeighbors=5)

                for (x,y,w,h) in faces:
                    roi_gray = gray[y:y + h, x:x + w]
                    id_, conf = recognizer.predict(roi_gray)
                    print("Face found")
                    print(path)

                    if conf >= 4 and conf <= 80:
                        name = labels[id_]
                        os.rename(path, os.path.join(root, name)) #path = C:\Users\delay\PycharmProjects\pythonProject\TheNewProject\Face Recognition\ToProcess\1, 0
                        print("Remapping")

                    else:
                        roi = image_array[y:y+h, x:x+w]
                        x_train.append(roi)
                        y_labels.append(id_)
                        print("training")


    with open("../labels.txt", 'wb') as f:
        pickle.dump(label_ids, f)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save(r"C:\Users\delay\PycharmProjects\pythonProject\TheNewProject\Face Recognition\trainner.yml")

facetrainer()
