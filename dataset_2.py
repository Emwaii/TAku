from imutils.video import VideoStream, FileVideoStream
import imutils
import time
import cv2
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import os

detector = cv2.CascadeClassifier("haar.xml")
vid = "C:/Users/Emwai/Pictures/testing/5.mp4"
vs = VideoStream(src=0).start()
# vs = FileVideoStream(vid).start()
time.sleep(1.0)

datasets ="dataset"

ROOT = tk.Tk()
ROOT.eval('tk::PlaceWindow . center')

ROOT.withdraw()
ROOT.wm_attributes("-topmost", True)    
nama = simpledialog.askstring(title="Name",prompt="Masukkan Nama?")

path = os.path.join(datasets, nama)
if not os.path.isdir(path):
    os.mkdir(path)

count = 1
while count <= 300:
    
    frame = vs.read()
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)

    rects = detector.detectMultiScale(gray, 
                        scaleFactor=1.2,
                        minNeighbors=5, 
                        minSize=(30,30),
                        flags=cv2.CASCADE_SCALE_IMAGE)
    
    cv2.putText(frame,'Gambar ke- %s' %(count)+"/300",(10,40), cv2.FONT_HERSHEY_PLAIN,1,(255, 255, 255),2)

    for (x,y,w,h) in rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (160, 160))
        cv2.imwrite('%s/%s.jpg' % (path,count), face_resize)
        count +=1
   
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(10) 
    if key == 27 & 0xFF == ord("q"):
        break
messagebox.showinfo("Info","Gambar berhasil disimpan")

cv2.destroyAllWindows()
vs.stop()