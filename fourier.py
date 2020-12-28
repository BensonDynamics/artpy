"""
First art concept. Nothing too sophisticated: Takes a generic line image,
performs an FFT, then generates a few different fourier transform related
grapics and animations.
"""

import numpy as np
import artpy as ap


def image_fft(img, kernelDim = 5):
    linedImage = ap.create_line_drawing_image(img, kernelDim)
    return np.fft(linedImage)


def fft_static(img, kernelDim = 5):
    transform = image_fft(img, kernelDim)

    for n in transform:




def fft_arm_animation(img, kernelDim=5):
    transform = image_fft(img, kernelDim)

    for n in transform:



def fft_refinement_animation(img, kernelDim=5):
    transform = image_fft(img, kernelDim)

    for n in transform:
