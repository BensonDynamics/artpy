import numpy as np
import matplotlib.pyplot as plt


class PathObject():
    """Create single path from a line-like image"""
    def __init__(self, imageArray, threshold = 50):
        self.imageArray = imageArray
        self.imageArray[self.imageArray > threshold] = 1

    def show(self):
        plt.imshow(self.imageArray)

    def tour(self):
        return

    def path(self):
        return

