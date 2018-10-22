from vpython import *
import math

""" Cubelet object class. Accepts a position of a 3-Dimensional vector 
    in the form of an (x, y , z) triplet containing a range of values from -1 to 1 """


class Cubelet(object):

    def __init__(self, pos, size, color):
        self.pos = {"x": pos[0], "y": pos[1], "z": pos[2]}
        self.size = {"length": size[0], "width": size[1], "height": size[2]}
        self.color = {"red" : color[0], "green" : color[1], "blue" : color[2]}
        cubelet = pyramid(pos=vector(self.pos["x"], self.pos["y"], self.pos["z"]),
                          color=vector(self.color["red"] , self.color["green"], self.color["blue"]),
                          size=vector(self.size["length"], self.size["width"], self.size["height"]))

        self.vertex = size[2]
        cubelet.rotate(angle=math.radians(270), axis=vec(self.vertex, 0, 0))


Cubelet((0, 0, 0), (1, 1, 1), (0, 0, 255))





