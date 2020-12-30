"""
First art concept. Nothing too sophisticated: Takes a generic line image,
performs an FFT, then generates a few different fourier transform related
grapics and animations.
"""

import numpy as np
import artpy as ap


def image_fft(line_img, kernelDim = 5):
    imgFFT = ap.create_line_drawing_image(line_img, kernelDim)
    return np.fft(imgFFT)


def fft_static(line_img, kernelDim = 5):
    transform = image_fft(line_img, kernelDim)

    #for n in transform:




def fft_arm_animation(line_img, kernelDim=5):
    transform = image_fft(line_img, kernelDim)

    #for n in transform:




def fft_refinement_animation(line_img, kernelDim=5):
    transform = image_fft(line_img, kernelDim)

    #for n in transform:
