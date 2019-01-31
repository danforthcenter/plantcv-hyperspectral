from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
import numpy as np
import matplotlib.pyplot as plt


def normalize_hyperspectral(hyper_array, reference_array_white, reference_array_dark, rows, cols, bands):
    """this function allows you read in hyperspectral images in raw format as array and normalize it with white and dark reference

    Inputs:
    hyper_array = the array format of the hyperspectral data
    reference_array_white = the array format of the white reference data
    reference_array_dark = the array format of the dark reference data
    cols = number of cols
    rows = number of rows
    bands = number of bands

    Returns:
    norm = normalized hyperspectral image
    one_channel = plots 10th channel of the normalized hyperspectral image (for visual purposes)

    """

<<<<<<< HEAD
    params.device += 1
=======
    device += 1
>>>>>>> read_hyperspectral_gdal

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
