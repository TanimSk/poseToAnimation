**how to use -**

    pip install opencv-python mediapipe
    git clone https://github.com/TanimSk/poseToAnimation
    cd poseToAnimation
    python main.py

**what it does -**  
tracks pose and generates a stick figure frame by frame.

**how does it work -**  
tracks with 33 pose landmarks using [ML model](https://github.com/google-research/google-research/tree/master/ghum) and returns the coordinates. Then generates a frame by connecting and manipulating the coords.

![enter image description here](https://google.github.io/mediapipe/images/mobile/pose_tracking_full_body_landmarks.png)

**why i need it -**  
you can generate stick figure animation for game development or just mess around with ML stuffs.

![Demo](https://github.com/TanimSk/poseToAnimation/blob/main/demo.png)
