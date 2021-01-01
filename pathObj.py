import numpy as np
import matplotlib.pyplot as plt
from

class PathObject():
    """Create single path from a line-like image"""
    def __init__(self, imageArray, threshold = 200, scale = 3):
        self.imageArray = imageArray
        self.imageArray[self.imageArray > threshold] = 1
        self.img_sm = self.imageArray.resize(tuple([int(v / scale) for v in self.imageArray.size]))

    def show(self):
        plt.imshow(self.imageArray)
        plt.show()

    def tour(self):
        return


    def path(self):
        return


