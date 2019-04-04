# calibrate raw image with white and dark references

from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
import numpy as np
import matplotlib.pyplot as plt


def calibrate_hs(image_array, reference_array_white, reference_array_dark, rows, cols, bands):

    """this function allows you read in hyperspectral images in raw format as array and normalize it with white and dark reference

    Inputs:
    image_array = image in array format
    reference_array_white = white reference data in array format
    reference_array_dark = dark reference data in array format
    cols = number of cols
    rows = number of rows
    bands = number of bands

    Returns:
    calibrated = calibrated hyperspectral image
    sample_channel = plots middle channel of the calibrated hyperspectral image (for visual purposes)

    :param image_array: numpy.ndarray
    :param reference_array_white: numpy.ndarray
    :param reference_array_dark: numpy.ndarray
    :param wavelength: list
    :param cols: int
    :param rows: int
    :param bands: int
    :return calibrated: numpy.ndarray
    :return sample_channel: numpy.ndarray
    """

    params.device += 1

    den = reference_array_white-reference_array_dark
    output_num = []
    for i in range(0,rows):
        ans = image_array[:,:,i]-reference_array_dark
        (output_num.append( (ans) ))
    num = np.stack(output_num, axis=2)
    output_calibrated = []
    for i in range(0,rows):
        ans1 = num[:,:,i]/den
        (output_calibrated.append( (ans1) ))
    calibrated1 = np.stack(output_calibrated, axis=2)
    calibrated = np.transpose(calibrated1[:,:,:], (2,1,0))
    sample_channel = calibrated[:,:, bands//2]
    plt.imshow(sample_channel)

    return calibrated, sample_channel
