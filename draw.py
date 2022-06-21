import numpy as np
import cv2 as cv


class Draw:
    def __init__(self, resolution, background_color, line_color):
        self.line_color = line_color                    # (0, 0, 0) -> black
        
        self.image = np.zeros((
            resolution[0], resolution[1], 4
        ), np.uint8)                                    # (x, y, 3) 3 -> 3 channels, RGB
        
        self.image[:] = background_color                     # [255, 255, 255] -> white

    def draw_line(self, start, end):
        self.image = cv.line(self.image, start, end, self.line_color, 3)

    def draw_head(self, position, radius):
        self.image = cv.circle(self.image, position, radius, self.line_color, -1)

    def generate(self):
        return self.image



