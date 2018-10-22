from vpython import *
import numpy as np

""" Cubelet object class. Accepts a position of a 3-Dimensional vector 
    in the form of an (x, y , z) triplet containing a range of values from -1 to 1 """


class Cubelet(object):

    def __init__(self, x, y, z, color):
        self.pos = {"x": x, "y": y, "z": z}
        self.red = color[0]
        self.green= color[1]
        self.blue= color[2]
        cubelet = pyramid(pos=vector(self.pos["x"], self.pos["y"], self.pos["z"]), color=vector(self.red, self.green, self.blue))

        if self.pos["y"] == 1:
            # print(2 + 2)
            cubelet.rotate(np.radians(270))


Cubelet(-1, -1, -1, (255, 0, 0))
Cubelet(0, -1, -1, (255, 0, 0))
Cubelet(1, -1, -1, (255, 0, 0))
Cubelet(-1, 0, -1, (0, 255, 0))
Cubelet(0, 0, -1, (0, 255, 0))
Cubelet(1, 0, -1, (0, 255, 0))
Cubelet(-1, 1, -1, (0, 0, 255))
Cubelet(0, 1, -1, (0, 0, 255))
Cubelet(1, 1, -1, (0, 0, 255))










