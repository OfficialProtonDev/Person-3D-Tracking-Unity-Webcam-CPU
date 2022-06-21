import cv2
import UdpComms as U
import time
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

visuals = True  # This will toggle the visiblity of the camera feed

IN = 1  # This will toggle the webcam source (0 = normal webcam, 1 = smartphone DroidCam webcam)

### ---------------------------------------------- Find person function -----------------------------------------------------
def getPerson(checkimage):

    checkimage.flags.writeable = False
    checkimage = cv2.cvtColor(checkimage, cv2.COLOR_BGR2RGB)
    results = pose.process(checkimage)
    checkimage.flags.writeable = True
    checkimage = cv2.cvtColor(checkimage, cv2.COLOR_RGB2BGR)

    x = []
    y = []
    z = []

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(checkimage, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, mp_drawing_styles.get_default_pose_landmarks_style() )
        for id, lm in enumerate(results.pose_landmarks.landmark):
              x.append(lm.x)
              y.append(checkimage.shape[0] - lm.y)
              z.append(lm.z)

    cv2.imshow("video", checkimage)
    return x, y, z           

### ---------------------------------------------- Main function -----------------------------------------------------
def useWebcam(IN=None):

    sock = U.UdpComms(udpIP="127.0.0.1", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=True)

    cap = cv2.VideoCapture(IN)

    while cap.isOpened():
        success, img = cap.read()

        if not success:
            print("No image found.")
            continue

        x, y, z = getPerson(img)

        if x and y and z != None:
            for i in range(33):
                strIn = "in" + str(i)
                sock.SendData(strIn)
                sock.SendData(str(x[i] * 10))
                sock.SendData(str(y[i] * 10))
                sock.SendData(str(z[i] * (10 / 3)))  

                

        elif x and y and z == None:
            sock.SendData("0")
            sock.SendData("0")
            sock.SendData("0")

        cv2.waitKey(1)
                



### -------------------  calling the main function-------------------------------

useWebcam(IN)




