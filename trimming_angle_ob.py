import os
import glob
import numpy as np
import re

class system:
    def mainsystem(dirname):
        f=Filemaneger()
        p=Picture
        files=f.get_directories()
        image=f.get_path(files)
        h,w=get_center(image)
        dst=andloop(image,h,w)
        save_image(dst)

class Filemaneger:
    def get_directories():
        pattern = ".*\.(jpg|png|bmp)"
        files = [f for f in os.listdir() if re.search(pattern, f, re.IGNORECASE)]
        return files

    def get_path():
        image=cv2.imread(image_path)

class Pictureeditor:
    def system(image):
        get_center()
        angloop()
        make_rectangle_on_face()
        save_image()

    def angle_change(image,h,w):
        matrix= cv2.getRotationMatrix2D((h,w), (num-10)*2, 1)
        dst=cv2.warpAffine(image, matrix, (100, 100))
        return dst

    def get_center(image):
        h=image.shape[0]/2
        w=image.shape[1]/2
        return h,w

    def make_rectangle_on_face():
        cascade_path="/usr/local/Cellar/opencv/3.4.1_2/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
        cascade=cv2.CascadeClassifier(cascade_path)
        facerect = cascade.detectMultiScale(dst,scaleFactor=1.1,minNeighbors=1,minSize=(1,1))
        if len(facerect) > 0:
            for rect in facerect:
                imagea = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
        return imagea

    def angloop(image,h,w):
        for num in range(20):
            return anglec_change(image,h,w)

    def save_image(dirname,imagea):
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        cv2.imwrite('neruf/'+image_path, imagea)

argvs = sys.argv
dirname=argvs[1]
s=system
s.mainsystem(dirname)

