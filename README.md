# 3D-Tracking-With-A-Single-Webcam-CPU-Only

Requirements:
 - A PC (no GPU required)
 - Unity
 - A smartphone / webcam
 
 What it is:
 -  This is a machine learning project that detects a persons joints in 3d space using only a single camera and sends the positions to unity to display in a 3d simulation
 
 Installation Instructions:
 
 - Download this repository.
 - Make sure you have Python 3.8 installed
 - Open cmd and cd into this repository.
 - Install required packages by running ``` pip install -r requirements.txt ```
 - Download Iriun Client on your PC and the Iriun app on your phone (if using a webcam ignore this)

 Customizable Settings:
 ```
 visuals = True  # This will toggle the visiblity of the camera feed

 IN = 1  # This will toggle the webcam source (0 = normal webcam, 1 = smartphone DroidCam webcam)
 ```

 How to use:
 
 - Open cmd and cd into this repository.
 - Run the command ``` python tracking.py ``` to start the program, make sure you have Iriun Client open and are connected to your phone via Wi-Fi or USB, while the Iriun app is open (if using a webcam ignore this)
 - Import the .unitypackage into a new unity project and open the tracking scene and press run. Make sure the webcam is pointed at you and you should see a series of connected joints matching your joints movements.
