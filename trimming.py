import cv2
import sys
import os.path
import os
import glob
argvs = sys.argv
cascade_path="/usr/local/Cellar/opencv/3.4.1_2/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
#files=os.listdir()
for x in os.listdir():
    image_path=x
    if os.path.isfile(x):
#image_pathh=argvs[1]
#image_path="test.jpg"
#color=(255,255,255)
            print(image_path)
            image=cv2.imread(image_path)
#image=cv2.imread(image_path)
#cv2.imshow("loaded",image)
#image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cascade=cv2.CascadeClassifier(cascade_path)
            facerect = cascade.detectMultiScale(image,scaleFactor=1.1,minNeighbors=1,minSize=(1,1))

#print ("face rectangle")
#print (facerect)

            if len(facerect) > 0:
                for rect in facerect:
                    image = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
    #顔が検出されなかった時
            else:
                print("no face")
#cv2.rectangle(image,tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]),color,thickness=2)
#cv2.imwrite("detected.jpg",image
#fileName=os.path.join(argvs[2],str(argvs[2]+"f.jpg")
#cv2.imwrite("out.jpg",image)
            dirname = argvs[1]
            if not os.path.exists(dirname):
                os.mkdir(dirname)
    #print('neru/'+argvs[1])
#cv2.imwrite(os.path.join(dirname, str(i)+'.jpg'), image)
            cv2.imwrite('neruf/'+image_path, image)


