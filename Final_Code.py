import cv2
import numpy as np
import os 
import datetime as dt
from datetime import timedelta,timezone,tzinfo,date
from datetime import datetime
import telepot
import telepot.namedtuple
from os import listdir
from os.path import isfile, join
from time import sleep
import imutils
import time
from imutils.video import VideoStream
from imutils.video import FileVideoStream
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import pandas as pd
import requests
import schedule
import random

# - Tkinter
ROOT = tk.Tk()
ROOT.eval('tk::PlaceWindow . center')
ROOT.withdraw()
ROOT.wm_attributes("-topmost", True)  

# - Data Training
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('train/train.yml')
faceCascade = cv2.CascadeClassifier("haar/face.xml")

font = cv2.FONT_HERSHEY_PLAIN

# - Inisialisasi Awal
id = 0
pesan = 0
wajah = 0
wajahh = 0
datasets = 'dataset'
pathunknow = 'unknown'
chatID = "-1001503911490" # - ID chat Bot MYHome (https://api.telegram.org/bot<YourBOTToken>/getUpdates)
# chatID = '1171747967' # - ID Chat Bot HammaXD
# tokenBot = '5018048140:AAEJRKJ0lSZg_AYubVgo3_o2XFCO4FouJcw' # - Token Bot HammaXD
tokenBot = '1883912262:AAEiiDgxCsVHT2pO26KXeu0RHhcnMbsKWPA' # - Token Bot MYHome
bot = telepot.Bot(tokenBot) # - Bot Token

# - Inisalisasi tanggal dan waktu
now = dt.datetime.now()
datenow = str(now.strftime("%d%m%Y"))
timenow = str(now.strftime("%H%M%S"))

start = dt.datetime.now()-timedelta(seconds=10)
end = dt.datetime.now()

# Mengambil nama dari folder direktori
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1

# (images, lables) = [np.array(lis) for lis in [images, lables]]  # i dont know

# - Mengambil nama gambar orang tidak diketahui
fileDir = os.path.dirname(__file__) + "/" + pathunknow + "/"   #direktori file

def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

# - Bot Telegram
def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + tokenBot + '/sendMessage?chat_id=' + chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def kirimGambar():

    bot.sendPhoto(chatID, photo=open(fileDir + "Unknown" + ".jpg", 'rb'))

def sendImage():

	nama = [f for f in listdir(pathunknow) if isfile(join(pathunknow, f))] #nama file
	for nama in nama:
		tgl = os.path.split(nama)[-1].split('.')[0]
		strtotime = datetime.strptime(tgl, "%d%m%Y%H%M%S")

		if time_in_range(start, end, strtotime):
			print (nama)
			bot.sendPhoto(chatID, photo=open(fileDir + nama, 'rb'))

	print (''.join(str(start).split('.')[0]),''.join(str(end).split('.')[0]))

schedule.every().hour.do(sendImage)

# - Mensetup kamera
vid = "C:/Users/Emwai/Pictures/testing/2.mp4"

# - Imutils capture
# cam = FileVideoStream(vid).start()
cam = VideoStream(src=0,framerate=30).start()

# - Opencv capture
# cam = cv2.VideoCapture(0)
# cam = cv2.VideoCapture(vid)
# time.sleep(2.0)

#- resize window camera cv2.videoCapture
# scale_percent = 70 # percent of original size
# width = int(cam.get(3) * scale_percent / 100)
# height = int(cam.get(4) * scale_percent / 100)
# dim = (width, height)

messagebox.showinfo("Info","Kamera Siap")

while True:
    
    frame = cam.read() #- Imutils
    # ret,frame = cam.read() #- CV2

    # - Konfigurasi frame
    # frame = cv2.flip(frame, 1) # Flip vertically
    frame = imutils.resize(frame, width=500) #- resize imutils
    # frame = cv2.resize(frame, (dim), interpolation = cv2.INTER_AREA) #- resize CV2
    
    # Detect the faces
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5, minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    
    for (x, y, w, h) in faces:
        # - Rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.rectangle(frame,(x, y-22),(x+w, y),(0, 255, 0),-1)
        cv2.rectangle(frame, (x, y-22), (x+w, y+h), (0, 255, 0), 2)

        # - Prediction
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (160, 160))
        prediction = recognizer.predict(face_resize)
        # print(prediction[1])
  
        if  prediction[1] <= 75:
            cv2.putText(frame,str(names[prediction[0]])+" "+str(round(100-prediction[1]))+"%",(x+5,y-6), font,1,(255, 255, 255))
            # cv2.imwrite("unknown/" +names[prediction[0]]+str(prediction[1])+".jpg",frame)   
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.rectangle(frame,(x, y-22),(x+w, y),(0, 0, 255),-1)  
            cv2.rectangle(frame, (x, y-22), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame,"Tidak Dikenali",(x+5,y-6), font,1,(255, 255, 255))

            if (wajah): # - Jika deteksi jumlah wajah bertambah
                wajah+=1               
                while pesan != 1:
                    pesan+=1
                    # cv2.imwrite("unknown/" +"Unknown"+".jpg",frame)
                    # bot.sendMessage(chatID, 'Tidak dikenali')
                    # kirimGambar()

                    # telegram_bot_sendtext("Orang tidak dikenal")
                    # time.sleep(1)

            wajah = len(faces)

    if (wajah==0) or (wajahh == wajah):
        p=0

    if (len(faces)):
        wajah += 1
        wajahh = wajah


    # - To do Schedule sendImage
    # schedule.run_pending()
    # time.sleep(1)
                
    # updateS = dt.datetime.now()-timedelta(seconds=10)
    # updateE = dt.datetime.now()
    # start = updateS
    # end = updateE
    
    cv2.imshow('Camera', frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# cam.release()
cv2.destroyAllWindows() 
cam.stop()
     
