from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import pigpio
from tkinter import *
from PIL import Image, ImageTk
pi = pigpio.pi()

print("[INFO] loading encodings + face detector...")
data = pickle.loads(open("encodings.pickle", "rb").read())
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
matkhau = "123456"
matkhaunhap = ""
matkhaufake = ""
bt_state = ""
bt_fake = ""
results = 0
who = ""
dem = 0
nhapsai = 0

tk = Tk()
tk.title("khoacua")
tk.geometry("450x290+0+0")
tk.resizable(0, 0)
tk.configure(background="white")

lb = Label(tk, fg="red", bg="white", font="Times 13", text="The University Of Technology And Education")
lb.pack()
lb.place(x=140, y=10)
lb = Label(tk, fg="blue", bg="white", font="Times 13", text="Smart Door Locks With Facial Recognition")
lb.pack()
lb.place(x=20, y=30)
lb = Label(tk, fg="black", bg="white", font="Times 13",
           text="------------------------------------------------------------------------------------------------------------------------------------")
lb.pack()
lb.place(x=0, y=55)

lb = Label(tk, fg="black", bg="white", font="Times 11", text="ENTER PASSWORD")
lb.pack()
lb.place(x=30, y=75)

lb = Label(tk, fg="green", bg="white", font="Times 12", text=matkhaufake)
lb.pack()
lb.place(x=30, y=91)

lb = Label(tk, fg="green", bg="white", font="Times 12", text="IDENTIFICATION CAMERA")
lb.pack()
lb.place(x=250, y=75)


def so1():
    global bt_state
    global matkhaunhap
    global matkhaufake
    bt_state = "1"
    bt_fake = "*"
    matkhaunhap = matkhaunhap + bt_state
    matkhaufake = matkhaufake + bt_fake


BT = Button(tk, text="1", bg="gray", height=3, width=4, command=so1)
BT.place(x=30, y=115)


def so2():
    global bt_state
    global matkhaunhap
    global matkhaufake
    bt_state = "2"
    bt_fake = "*"
    matkhaunhap = matkhaunhap + bt_state
    matkhaufake = matkhaufake + bt_fake


BT = Button(tk, text="2", bg="gray", height=3, width=4, command=so2)
BT.place(x=80, y=115)


def so3():
    global bt_state
    global matkhaunhap
    global matkhaufake
    bt_state = "3"
    bt_fake = "*"
    matkhaunhap = matkhaunhap + bt_state
    matkhaufake = matkhaufake + bt_fake


BT = Button(tk, text="3", bg="gray", height=3, width=4, command=so3)
BT.place(x=130, y=115)


def so4():
    global bt_state
    global matkhaunhap
    global matkhaufake
    bt_state = "4"
    bt_fake = "*"
    matkhaunhap = matkhaunhap + bt_state
    matkhaufake = matkhaufake + bt_fake


BT = Button(tk, text="4", bg="gray", height=3, width=4, command=so4)
BT.place(x=30, y=150)


def so5():
    global bt_state
    global matkhaunhap
    global matkhaufake
    bt_state = "5"
    bt_fake = "*"
    matkhaunhap = matkhaunhap + bt_state
    matkhaufake = matkhaufake + bt_fake


BT = Button(tk, text="5", bg="gray", height=3, width=4, command=so5)
BT.place(x=80, y=150)


def so6():
    global bt_state
    global matkhaunhap
    global matkhaufake
    bt_state = "6"
    bt_fake = "*"
    matkhaunhap = matkhaunhap + bt_state
    matkhaufake = matkhaufake + bt_fake


BT = Button(tk, text="6", bg="gray", height=3, width=4, command=so6)
BT.place(x=130, y=150)


def so7():
    global bt_state
    global matkhaunhap
    global matkhaufake
    bt_state = "7"
    bt_fake = "*"
    matkhaunhap = matkhaunhap + bt_state
    matkhaufake = matkhaufake + bt_fake


BT = Button(tk, text="7", bg="gray", height=3, width=4, command=so7)
BT.place(x=30, y=185)


def so8():
    global bt_state
    global matkhaunhap
    global matkhaufake
    bt_state = "8"
    bt_fake = "*"
    matkhaunhap = matkhaunhap + bt_state
    matkhaufake = matkhaufake + bt_fake


BT = Button(tk, text="8", bg="gray", height=3, width=4, command=so8)
BT.place(x=80, y=185)


def so9():
    global bt_state
    global matkhaunhap
    global matkhaufake
    bt_state = "9"
    bt_fake = "*"
    matkhaunhap = matkhaunhap + bt_state
    matkhaufake = matkhaufake + bt_fake


BT = Button(tk, text="9", bg="gray", height=3, width=4, command=so9)
BT.place(x=130, y=185)


def sox():
    global bt_state
    global matkhaunhap
    global matkhaufake
    matkhaunhap = matkhaunhap[:-1]
    matkhaufake = matkhaufake[:-1]
    lb = Label(tk, fg="black", bg="white", font="Times 13", text="                        ")
    lb.pack()
    lb.place(x=30, y=91)


BT = Button(tk, text="x", bg="red", height=3, width=4, command=sox)
BT.place(x=30, y=220)


def so0():
    global bt_state
    global matkhaunhap
    global matkhaufake
    bt_state = "0"
    bt_fake = "*"
    matkhaunhap = matkhaunhap + bt_state
    matkhaufake = matkhaufake + bt_fake


BT = Button(tk, text="0", bg="gray", height=3, width=4, command=so0)
BT.place(x=80, y=220)


def soo():
    global bt_state
    global matkhaunhap
    global matkhaufake
    global nhapsai
    nhapsai = nhapsai+1
    if nhapsai == 5:
        pi.write(26, 1)
        time.sleep(10)
        pi.write(26, 0)
        nhapsai = 0
    bt_state = "o"
    lb = Label(tk, fg="black", bg="white", font="Times 13", text="                        ")
    lb.pack()
    lb.place(x=30, y=91)
    print(matkhaufake)


BT = Button(tk, text="o", bg="green", height=3, width=4, command=soo)
BT.place(x=130, y=220)

servo_1 = 13
pi.set_mode(servo_1, pigpio.OUTPUT)
pi.set_servo_pulsewidth(servo_1, 1000)

pi.set_mode(26, pigpio.OUTPUT)
pi.write(26, 0)

vs = VideoStream(src=0).start()
time.sleep(1.0)


def nhandang_km():
    global who
    global results
    frame = vs.read()
    frame = imutils.resize(frame, width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # detect faces in the grayscale frame
    rects = detector.detectMultiScale(gray, scaleFactor=1.1,
                                      minNeighbors=5, minSize=(30, 30),
                                      flags=cv2.CASCADE_SCALE_IMAGE)
    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []
    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding,0.4)
        print(matches)
        name = "Unknown"
        if True in matches:
            print("ok")
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
                name = max(counts, key=counts.get)
        names.append(name)
    for ((top, right, bottom, left), name) in zip(boxes, names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, f'{name}', (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
        who = name
        cv2.imwrite('frame.jpg', frame)
        imagelg = Image.open('frame.jpg')
        imagelg = imagelg.resize((190, 140), Image.ANTIALIAS)
        imagelg = ImageTk.PhotoImage(imagelg)
        lb03 = Label(image=imagelg)
        lb03.image = imagelg
        lb03.pack()
        lb03.place(x=250, y=115)
while True:
    nhandang_km()
    if who == "Truong":
        dem = dem + 1
    if who == "Phuong":
        dem = dem + 1
    if who == "Dieu":
        dem = dem + 1
    if who == "Vuong":
        dem = dem + 1
    if matkhaunhap == matkhau and bt_state == "o" or dem == 10:
        nhapsai = 0
        pi.write(26, 1)
        time.sleep(0.1)
        pi.write(26, 0)
        time.sleep(0.05)
        pi.write(26, 1)
        time.sleep(0.1)
        pi.write(26, 0)
        for x in range(1000, 2000, 1):
            pi.set_servo_pulsewidth(servo_1, x)
            time.sleep(0.0001)
        time.sleep(3)
        for x in range(2000, 1000, -1):
            pi.set_servo_pulsewidth(servo_1, x)
            time.sleep(0.0001)
        matkhaunhap = ""
        matkhaufake = ""
        who = ""
        dem = 0
    lb = Label(tk, fg="green", bg="white", font="Times 13", text=matkhaufake)
    lb.pack()
    lb.place(x=30, y=91)
    tk.update()
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()

