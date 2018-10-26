import os
from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
import numpy as np
import matplotlib.pyplot as plt


def normalize_hyperspectral(hyper_array, reference_array_white, reference_array_dark, rows, cols, bands):
    """this function allows you read in hyperspectral images in raw format as array (needs associated .hdr file)

    Inputs:
    path     = path to .hdr file, there is the assumption that .hdr file name matches raw image name

    Returns:
    gdalhyper = hyperspectral image
    immage_array = averag of hyperspectral image as array
    cols = number of cols
    rows = number of rows
    bands = number of bands


    :param hyperimg: spectral object
    :param bands: list of band centers
    :param path: string
    :return filname: string
    """

    device += 1

    image_array_trans = np.transpose(image_array_all[:,:,:], (0,2,1))
    den = image_array_white-image_array_dark
    output_num = []
    for i in range(0,rows):
        ans = image_array_trans[:,:,i]-image_array_dark
        (output_num.append( (ans) ))
    num = np.stack(output_num, axis=2)
    output_norm = [] #[cols, rows, bands]
    for i in range(0,rows):
        ans1 = num[:,:,i]/den
        (output_norm.append( (ans1) ))
    norm = np.stack(output_norm, axis=2)
    normz = np.transpose(norm[:,:,:], (2,1,0))
    print(normz.shape)
    one_channel = normz[:,:,10]
    plt.imshow(one_channel)
    return norm, one_channel
