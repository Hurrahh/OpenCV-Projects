import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
draw = mp.solutions.drawing_utils

ptime = 0
ctime = 0
while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                print(id,lm)
                height, width, channel = img.shape
                cx, cy = int(lm.x*width), int(lm.y*height)

                if id == 4:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

            draw.draw_landmarks(img,handLms,mphands.HAND_CONNECTIONS)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_DUPLEX,3,(255,0,255),3)


    cv2.imshow("Hand Tracking",img)
    cv2.waitKey(1)