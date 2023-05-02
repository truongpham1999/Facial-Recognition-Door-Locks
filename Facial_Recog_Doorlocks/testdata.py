import pickle
import numpy as np
import os
import face_recognition
import cv2
from sklearn.metrics import classification_report
from glob import glob
from sklearn.metrics import classification_report

file = open("encodings.pickle", 'rb')
data = pickle.load(file)
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def detectFace(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (300, 300))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rects = detector.detectMultiScale(gray, scaleFactor=1.1,
                                      minNeighbors=5, minSize=(30, 30),
                                      flags=cv2.CASCADE_SCALE_IMAGE)
    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []
    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance=0.35)
        # print(matches)
        name = "Unknown"
        if True in matches:
            # print("ok")
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
                name = max(counts, key=counts.get)
        names.append(name)
    return names


# lb = detectFace("ronaldo.jpg")
# print(lb)
def detect(img_folder):
    predicted_label = []
    list_imgDir = glob(img_folder + "/*")
    for imgDir in list_imgDir:
        lb = detectFace(imgDir)
        predicted_label.append(lb)
    return predicted_label


print("Start testing: ....")
root = "./DATAFORTEST/"
lb = os.listdir("./DATAFORTEST")
pred = []
true_label = []
for name in lb:
    true = []
    dt_path = root + str(name)
    for i in range(len(glob(dt_path + "/*"))):
        true.append(name)
    true_label.append(true)
    pred.append(detect(dt_path))
# print(len(true_label))
# print(pred)

truong = 0
dieu = 0
phuong = 0
vuong = 0
unknown = 0


print("Analyze Result:....")

for j in range(25):
    if (pred[0][j] == []):
        continue
    if (pred[1][j] == []):
        continue
    if (pred[2][j] == []):
        continue
    if (pred[3][j] == []):
        continue
    if (pred[0][j][0]) == "Dieu":
        dieu += 1
    if (pred[1][j][0]) == "Phuong":
        phuong += 1
    if (pred[2][j][0]) == "Truong":
        truong += 1
    if (pred[3][j][0]) == "Vuong":
        vuong += 1

print("Output:")
f = open("output.txt", "w")

f.write("Accuracy for each class: \n")
f.write("Truong: " + str(truong / 25) + "\n")
f.write("Phuong: " + str(phuong / 25) + "\n")
f.write("Vuong: " + str(vuong / 25) + "\n")
f.write("Dieu: " + str(dieu / 25) + "\n")
f.write("Accuracy: " + str((truong + phuong + vuong + dieu) / 100))

f.close()

print("Accuracy for each class:")
print("Truong: ", str(truong /25))
print("Phuong: ", str(phuong /25 ))
print("Vuong: ", str(vuong  /25))
print("Dieu: ", str(dieu /25 ))
print("Accuracy: ", str((truong + phuong + vuong + dieu) /100))

# true_label = flatten(true_label)
# pred = flatten(pred)
# print(true_label)
# print(pred)


# print(classification_report(true_label, pred))