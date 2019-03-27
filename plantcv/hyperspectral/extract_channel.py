# extract any channel from the hyperspectral array

import numpy as np
from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
import matplotlib.pyplot as plt



"""Reads the hyperspectral image and converts it to array, reads the metadata and extracts the wavelength

    Inputs:
    a = lower range of wavelength to extract
    b = higher range of wavelength to extract
    wavelength = the list of wavelengths


    Returns:
    channelsum = average value of reflectance in the given range

    :param a: int
    :param b: int
    :return channelsum: numpy.ndarray 
    

    """
    params.device += 1


def extract_channel(a, b, wavelength)

    if array is None:
        fatal_error("Failed to open " + array)

    channel = [i for i in wavelength if i>=a and i<=b]
    indchannel = []
    for i in channel:
        d = wavelength.index(i)
        (indchannel.append( (d) ))
    channel1 = image_array_trans[indchannel[0]:indchannel[-1]]
    channelsum = np.sum(channel1, axis=0)
    if params.debug == 'print':
        plt.imsave(os.path.join(params.debug_outdir, str(params.device) + '_extracted' + '.png'), channelsum)
    elif params.debug == 'plot':
        plt.imshow(channelsum, cmap='gray')
    return channelsum
