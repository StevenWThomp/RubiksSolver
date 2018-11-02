from vpython import *
import math

""" Cubelet object class. Accepts a position, size, and color argument. Each in the form of a 3-dimensional vector 
                                                        Arguments:
                                    pos: (x, y, z) values ranging from -1 to 1.
                                    color: (0-255, 0-255, 0-255) Accepts a color values in the form of an RGB triplet.
                                    OPTIONAL - size: (Length, Width, Height) Default values are (1, 1, 1) """


class Cubelet(object):

    def __init__(self, pos, color):

        self.pos = vector(pos[0], pos[1], pos[2])  # {"x": , "y": , "z": }
        self.color = vector(color[0], color[1], color[2])  # {"red": , "green": , "blue": }
        self.vertex = vector(1, pos[1], pos[2])

        horizontal = pyramid(pos=self.pos, color=self.color)
        vertical = pyramid(pos=vector(pos[0], pos[1]-1, pos[2]), color=self.color)
        vertical.rotate(angle=math.radians(45), origin=self.vertex)
        vertical.rotate(angle=math.radians(45), axis=self.vertex)

        """                               MAYBE LATER
        if size is None:
                    self.size = (1, 1, 1)  # {"length": 1, "width": 1, "height": 1}
                else:
                    self.size = vertex(size[0], size[1], size[2])
        """


Cubelet((0, 0, 0), (255, 255, 255))



