import cv2, sys, numpy, os
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

haar_file = 'haar.xml'
datasets = 'dataset'

ROOT = tk.Tk()
ROOT.eval('tk::PlaceWindow . center')

ROOT.withdraw()
ROOT.wm_attributes("-topmost", True)   
messagebox.showinfo("Info","Trainning Dataset")

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
(width, height) = (160, 160)

(images, lables) = [numpy.array(lis) for lis in [images, lables]]

model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, lables)
model.write('train/train.yml')

messagebox.showinfo("Info","Trainning selesai {0} wajah telah dilatih".format(len(numpy.unique(lables))))