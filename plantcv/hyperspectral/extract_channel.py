# extract any channel from the hyperspectral array

import os
import numpy as np
from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
import matplotlib.pyplot as plt
from plantcv.plantcv import params




def extract_channel(a, b, image_array, wavelength):

    """Reads the array form of hyperspectral image and extracts the desired channel by giving the wavelength range
    Inputs:
    a = lower range of wavelength to extract
    b = higher range of wavelength to extract
    image_array = image in array format
    wavelength = the list of wavelengths


    Returns:
    channelsum = average value of reflectance in the given range

    :param a: int
    :param b: int
    :param image_array: numpy.ndarray
    :param wavelength: list
    :return channelsum: numpy.ndarray
    """

    params.device += 1

    if a > b:
        fatal_error("insert a as lower value and b as higher value")

    minwl = int(np.min(wavelength))
    maxwl = int(np.max(wavelength))
    if a < minwl:
       fatal_error("a is out of wavelength range")
    if b > maxwl:
       fatal_error("b is out of wavelength range")


    channel = [float(i) for i in wavelength if float(i) >= float(a) and float(i) <= float(b)]
    indchannel = []
    for i in channel:
        d = wavelength.index(i)
        (indchannel.append( (d) ))
    channel1 = image_array[indchannel[0]:indchannel[-1]]
    channelsum = np.sum(channel1, axis=0)
    if params.debug == 'print':
        plt.imsave(os.path.join(params.debug_outdir, str(params.device) + '_extracted' + '.png'), channelsum)
    elif params.debug == 'plot':
        plt.imshow(channelsum, cmap='gray')
    return channelsum
