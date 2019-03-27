# read hyperspectral image and metadata

import numpy as np
from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
from osgeo import gdal
from spectral import *

"""Reads the hyperspectral image and converts it to array, reads the metadata and extracts the wavelength

    Inputs:
    path_file      = path to the hyperspectral file
    path_wl         = path to the metadata containing wavelength


    Returns:
    image_array = image in array format
    cols = number of columns (image pixel resolution)
    rows = numbers of rows (image pixel resolution)
    bands = number of channels
    wavelength = wavelengths in list

    :param path_file: str
    :param path: str
    :return image_array: numpy.ndarray
    :return cols: int
    :return rows: int
    :return bands: int
    :return wavelength: list

    """
    params.device += 1


def hyper2array(path_file, path_wl):


    if array is None:
        fatal_error("Failed to open " + array)
    # reads metadata
    hyperhdr=spectral.open_image(path_wl)

    # reads hyperspectral data
    gdalhyper = gdal.Open(path_file)

    # converts hyperspectral data to array
    hyper_array = gdalhyper.ReadAsArray()

    # extracts shape of the array
    cols = gdalhyper.RasterXSize
    rows = gdalhyper.RasterYSize
    bands = gdalhyper.RasterCount

    # transposes the array to represent it in a correct way
    image_array = np.transpose(hyper_array[:,:,:], (0,2,1))

    # extract the wavelength
    wavelength = hyperhdr.bands.centers

    return image_array, cols, rows, bands, wavelength

