import numpy as np
import matplotlib.pyplot as plt


class PathObject():
    """Create single path from a line-like image"""
    def __init__(self, imageArray, threshold = 50):
        self.imageArray = imageArray
        for i in range(len(self.imageArray)):
            for j in range(len(self.imageArray[0])):
                if self.imageArray[i][j] > threshold:
                    self.imageArray[i][j] = 1
                else:
                    self.imageArray[i][j] = 0

    def show(self):
        plt.imshow(self.imageArray)

    def tour(self):
        return

    def path(self):
        return

