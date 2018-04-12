import cv2
import sys
import os.path
import os
import glob
import numpy as np
import re

pattern = ".*\.(jpg|png|bmp)"
files = [f for f in os.listdir() if re.search(pattern, f, re.IGNORECASE)]
argvs = sys.argv
#cascade_path="/usr/local/Cellar/opencv/3.4.1_2/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
#cascade_path="C:\Users\Kunisawa\Anaconda3\envs\openCV\Library\etc\haarcascades"
#for x in os.listdir():
cascade_path=argvs[2]
for x in files:
    image_path=x
    print(image_path)
    if os.path.isfile(x):
        for num in range(20):
            image=cv2.imread(image_path)
            cascade=cv2.CascadeClassifier(cascade_path)
            print(image_path)
            h=image.shape[0]/2
            w=image.shape[1]/2
            #size = tuple(image.shape[1], image.shape[0])
            #center = tuple(np.array(image.shape[1]*0.5, image.shape[0]*0.5))
            matrix= cv2.getRotationMatrix2D((h,w), (num-10)*2, 1)
            dst=cv2.warpAffine(image, matrix, (100, 100))
            facerect = cascade.detectMultiScale(dst,scaleFactor=1.1,minNeighbors=1,minSize=(1,1))
            if len(facerect) > 0:
                for rect in facerect:
                    imagea = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
                dirname = argvs[1]
                if not os.path.exists(dirname):
                    os.mkdir(dirname)
                cv2.imwrite('neruf/'+image_path, imagea)
            else:
                print("no face")


