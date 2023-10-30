# 3D-Tracking-With-A-Single-Webcam-CPU-Only

Requirements:
 - A PC (no GPU required)
 - Unity
 - A smartphone / webcam
 
 What it is:
 -  This is a machine learning project that detects a persons joints in 3d space using only a single camera and sends the positions to unity to display in a 3d simulation

 Demo:

https://user-images.githubusercontent.com/98558514/174703832-1d3f58a3-610f-4eb9-9d4f-cc509d1f4234.mp4

 Installation Instructions:
 
 - Download this repository.
 - Make sure you have Python 3.8 installed
 - Open cmd and cd into this repository.
 - Install required packages by running ``` pip install -r requirements.txt ```
 - Download Iriun on your PC and the Iriun app on your phone (if using a webcam ignore this)

 Customizable Settings:
 ```
 visuals = True  # This will toggle the visiblity of the camera feed

 IN = 1  # This will toggle the webcam source (0 = normal webcam, 1 = smartphone Iriun webcam)
 ```

 How to use:
 
 - Open cmd and cd into this repository.
 - Run the command ``` python person_tracking.py ``` for person detection or ``` python hand_tracking.py ``` for hand tracking, make sure you have Iriun open on your PC + phone and are connected to the same Wi-FI network as your phone (if using a webcam ignore this)
 - Import the .unitypackage into a new unity project and open the person / hand tracking scene and press run. Make sure the webcam is pointed at you and you should see a series of connected joints matching your joints movements.

# Credits:

Two-way communication between Python 3 and Unity (C#) - Y. T. Elashry
