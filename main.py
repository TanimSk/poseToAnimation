import cv2
import mediapipe as mp
from draw import Draw
import math


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


# ---------- GET Vertices --------

class Vertices:

    def __init__(self, width, height):
        self.image_width = width
        self.image_height = height

        self.point_a = self.PointA()
        self.point_b = self.PointB()

        self.point_a.x = (results.pose_landmarks.landmark[24].x + results.pose_landmarks.landmark[23].x) / 2
        self.point_a.y = (results.pose_landmarks.landmark[24].y + results.pose_landmarks.landmark[23].y) / 2

        self.point_b.x = (results.pose_landmarks.landmark[11].x + results.pose_landmarks.landmark[12].x) / 2
        self.point_b.y = (results.pose_landmarks.landmark[11].y + results.pose_landmarks.landmark[12].y) / 2

    def get_vertices(self, index):

        if index == 'A':
            return self.point_a

        elif index == 'B':
            return self.point_b

        else:
            return results.pose_landmarks.landmark[index]

    def calculate_distance(self, x1, y1, x2, y2):
        return int((math.sqrt(((x2*self.image_width) - (x1*self.image_width)) ** 2 + ((y2*self.image_height) - (y1*self.image_height)) ** 2)) / 2.5)

    class PointA:
        def __int__(self):
            self.x = None
            self.y = None

    class PointB:
        def __int__(self):
            self.x = None
            self.y = None



cap = cv2.VideoCapture('https://assets.mixkit.co/videos/preview/mixkit-young-man-walking-listening-to-music-from-his-headphones-4855-large.mp4')

index = 0

with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            break

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image_height, image_width, _ = image.shape
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        if results.pose_landmarks:
            # ---------------- GENERATE IMAGE -----------------
            trace_leg = [32, 30, 28, 26, 'A', 25, 27, 29, 31]
            trace_body = ['A', 'B']
            trace_hand = [20, 16, 14, 'B', 13, 15, 19]
            trace_head = ['B', 0]

            # init canvas
            draw_img = Draw([image_height, image_width], [255, 255, 255, 0], (0, 0, 0, 255))

            vertices = Vertices(image_width, image_height)

            # draw leg
            for i in range(len(trace_leg) - 1):
                start = (
                    int(vertices.get_vertices(trace_leg[i]).x * image_width),
                    int(vertices.get_vertices(trace_leg[i]).y * image_height)
                )

                end = (
                    int(vertices.get_vertices(trace_leg[i + 1]).x * image_width),
                    int(vertices.get_vertices(trace_leg[i + 1]).y * image_height)
                )

                draw_img.draw_line(start, end)

            # draw body
            for i in range(len(trace_body) - 1):
                start = (
                    int(vertices.get_vertices(trace_body[i]).x * image_width),
                    int(vertices.get_vertices(trace_body[i]).y * image_height)
                )

                end = (
                    int(vertices.get_vertices(trace_body[i + 1]).x * image_width),
                    int(vertices.get_vertices(trace_body[i + 1]).y * image_height)
                )

                draw_img.draw_line(start, end)

            # draw hand
            for i in range(len(trace_hand) - 1):
                start = (
                    int(vertices.get_vertices(trace_hand[i]).x * image_width),
                    int(vertices.get_vertices(trace_hand[i]).y * image_height)
                )

                end = (
                    int(vertices.get_vertices(trace_hand[i + 1]).x * image_width),
                    int(vertices.get_vertices(trace_hand[i + 1]).y * image_height)
                )

                draw_img.draw_line(start, end)

            # draw head
            for i in range(len(trace_head) - 1):
                start = (
                    int(vertices.get_vertices(trace_head[i]).x * image_width),
                    int(vertices.get_vertices(trace_head[i]).y * image_height)
                )

                end = (
                    int(vertices.get_vertices(trace_head[i + 1]).x * image_width),
                    int(vertices.get_vertices(trace_head[i + 1]).y * image_height)
                )

                draw_img.draw_line(start, end)

            draw_img.draw_head(
                (int(results.pose_landmarks.landmark[0].x * image_width), int(results.pose_landmarks.landmark[0].y * image_height)),
                52
            )

            img = draw_img.generate()

            cv2.imshow('MediaPipe Pose', img)
            index += 1
            cv2.imwrite(f'./frames/img{index}.png', img)

            if cv2.waitKey(5) & 0xFF == 27:
                break

cap.release()
