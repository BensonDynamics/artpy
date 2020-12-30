"""
First art concept. Nothing too sophisticated: Takes a generic line image,
performs an FFT, then generates a few different fourier transform related
grapics and animations.
"""

import numpy as np
import artpy.lineDrawing


def image_fft(line_img, kernelDim = 5):
    imgFFT = artpy.lineDrawing.create_line_drawing_image(line_img, kernelDim)
    return np.fft.rfft(imgFFT)[0]

def fft_draw(fft, n = len(fft), time_range = np.linspace(0,2*np.pi,1000), color = 'b'):
    freq_coef = np.arange(0, n)
    XY = np.ones((len(time_range),2))
    for t in time_range:
        XY[t][:] = [np.sum(fft*np.cos(freq_coef*t)), np.sum(fft*np.sin(freq_coef*t))
    return XY
