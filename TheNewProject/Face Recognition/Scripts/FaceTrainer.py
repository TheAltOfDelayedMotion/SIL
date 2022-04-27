import ast
import os
import pickle
from PIL import Image
import numpy as np
import cv2
import Directory

###############################################################################################################################
print("###############################################################################################################################\n\n"
      "Directory verification in progress..... \nOpening files...")

trainneryml = os.path.join(Directory.datadir, "trainner.yml")
labelstxt = os.path.join(Directory.datadir, "labels.txt")
timgdir = Directory.timgdir
pimgdir = Directory.pimgdir

with open(labelstxt, 'rb') as f:
    _labels = pickle.load(f)
    labels = {v: k for k, v in _labels.items()}

    print(_labels)

print("Process 1 is finished \n\n"
      "###############################################################################################################################")

###############################################################################################################################

def facetrainer():
    face_cascade = cv2.CascadeClassifier(os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(trainneryml)

    image_dir = Directory.pimgdir #os.path.dirname(os.path.abspath(__file__))
    current_id = 0
    label_ids = {}

    y_labels = []
    x_train = []

    print("\nTraining Process Started..... \n "
          "\n###############################################################################################################################")
    loopcount = 0

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(pimgdir, file)
                label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
                loopcount = loopcount + 1

                print("Picture Found... \n")

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

                for (x, y, w, h) in faces:
                    print("Face found in picture: " + path)
                    roi_gray = gray[y:y + h, x:x + w]
                    id_, conf = recognizer.predict(roi_gray)

                    if conf >= 4 and conf <= 80:
                        name = labels[id_]
                        print("Existing face, Remapping to.... " + name +
                              "\n\n###############################################################################################################################")

                        remapdircount = 0

                        while True:
                            remapimgdir = os.path.join(timgdir, name, str(remapdircount) + ".jpg")

                            if os.path.exists(remapimgdir):
                                remapdircount = remapdircount + 1

                            else:
                                os.rename(path, os.path.join(timgdir, name, str(remapdircount) + ".jpg"))  # path = C:\Users\delay\PycharmProjects\pythonProject\TheNewProject\Face Recognition\ToProcess\1, 0
                                break

                    elif conf >= 80 and conf <= 150:

                        print("Unidentified face, Training.... Conf: " + str(conf) +
                              "\n" + "\n###############################################################################################################################")

                        roi = image_array[y:y + h, x:x + w]
                        x_train.append(roi)
                        y_labels.append(id_)
                        mdirpcount = 0

                        while True:
                            mdirp = os.path.join(Directory.timgdir, str(mdirpcount))

                            if os.path.exists(mdirp):
                                mdirpcount = mdirpcount + 1

                            else:
                                os.makedirs(mdirp)
                                pictureid = 0

                                while True:
                                    if os.path.exists(os.path.join(mdirp, str(pictureid) + ".jpg")): #pictureid+png
                                        pictureid = pictureid + 1

                                    else:
                                        os.rename(path, os.path.join(mdirp, str(pictureid) + ".jpg"))

                                        with open(labelstxt, 'wb') as f:
                                            pickle.dump(label_ids, f)

                                        recognizer.train(x_train, np.array(y_labels))
                                        recognizer.save(trainneryml)

                                        break
                                break

                    else:
                        os.remove(path)
                        print("Spam, Deleting " + str(conf) +
                              "\n" + "\n###############################################################################################################################")
                try:
                    os.remove(path)
                    print("Spam, Deleting " 
                        "\n" + "\n###############################################################################################################################")

                except:
                    print("file not found")


facetrainer()

'''
###############################################################################################################################
Face found in picture: C:\Users\delay\PycharmProjects\pythonProject\TheNewProject\Face Recognition\ToProcess\221.jpg
Unidentified face, Training.... Conf: 126.50583951547996

###############################################################################################################################
Traceback (most recent call last):
  File "C:\Users\delay\PycharmProjects\pythonProject\TheNewProject\Face Recognition\Scripts\FaceTrainer.py", line 140, in <module>
    facetrainer()
  File "C:\Users\delay\PycharmProjects\pythonProject\TheNewProject\Face Recognition\Scripts\FaceTrainer.py", line 116, in facetrainer
    os.rename(path, os.path.join(mdirp, str(pictureid) + ".jpg"))
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\Users\\delay\\PycharmProjects\\pythonProject\\TheNewProject\\Face Recognition\\ToProcess\\221.jpg' -> 'C:\\Users\\delay\\PycharmProjects\\pythonProject\\TheNewProject\\Face Recognition\\TrainedFaces\\4\\0.jpg'

Process finished with exit code 1

'''