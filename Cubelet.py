from vpython import *
import math

""" Cubelet object class. Accepts a position, size, and color argument. Each in the form of a 3-dimensional vector 
                                                        Arguments:
                                    pos: (x, y, z) values ranging from -1 to 1
                                    color: (0-255, 0-255, 0-255) Accepts a color values in the form of an RGB triplet
                                    OPTIONAL - size: (Length, Width, Height) Default values are (1, 1, 1) """


class Cubelet(object):

    def __init__(self, pos, color, size=None):

        self.pos = {"x": pos[0], "y": pos[1], "z": pos[2]}
        self.color = {"red": color[0], "green": color[1], "blue": color[2]}
        self.size = size
        self.theta = 0
        if self.size is None:
            self.size = {"length": 1, "width": 1, "height": 1}
        else:
            self.size = {"length": size[0], "width": size[1], "height": size[2]}

        self.vertex = vector(self.size["height"], self.pos["y"], self.pos["x"])

        cubelet = pyramid(pos=vector(self.pos["x"], self.pos["y"], self.pos["z"]),
                          color=vector(self.color["red"], self.color["green"], self.color["blue"]),
                          size=vector(self.size["length"], self.size["width"], self.size["height"]))


Cubelet((0, 0, 0), (255, 255, 255))



