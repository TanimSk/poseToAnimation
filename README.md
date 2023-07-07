**Demo Video -**
https://www.youtube.com/watch?v=FMKiek_8b6s

**How to use -**

    pip install opencv-python mediapipe
    git clone https://github.com/TanimSk/poseToAnimation
    cd poseToAnimation
    python main.py

**what it does -**  
tracks pose and generates stick figure frame by frame.

**how does it work -**  
tracks with 33 pose landmarks using [ML model](https://github.com/google-research/google-research/tree/master/ghum) and returns the coordinates. Then generates a frame by connecting and manipulating the coords.

![MediaPipe](https://developers.google.com/static/mediapipe/images/solutions/pose_landmarks_index.png)

**why i need it -**  
you can generate stick figure animation for game development or just mess around with ML stuffs.

![Demo](https://github.com/TanimSk/poseToAnimation/blob/main/demo.png)
