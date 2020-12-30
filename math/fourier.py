"""
First art concept. Nothing too sophisticated: Takes a generic line image,
performs an FFT, then generates a few different fourier transform related
grapics and animations.
"""

import numpy as np

def image_fft(line_img):
    return np.fft.rfft(line_img)[0]

def fourier_draw(fft, n = -1, time_range = np.linspace(0,2*np.pi,1000),
                 color = 'b'):
    if n<0:
        n=len(fft)

    freq_coef = np.arange(0, n)
    XY = np.ones((len(time_range),2))
    for t in time_range:
        XY[t][:] = [np.sum(np.multiply(fft, np.cos(freq_coef*t))),
                    np.sum(np.multiply(fft, np.sin(freq_coef*t)))]
    return XY
