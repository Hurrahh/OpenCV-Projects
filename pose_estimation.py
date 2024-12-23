import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)
ptime = 0
mppose = mp.solutions.pose
pose = mppose.Pose()

while True:
    success,img = cap.read()
    cv2.imshow("Image",img)
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = pose.process(imgRGB)



    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_DUPLEX,2,(255,0,255),3)

    cv2.waitKey(1)