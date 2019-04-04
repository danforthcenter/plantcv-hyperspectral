# read reference image

import os
import numpy as np
from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
from osgeo import gdal
from spectral import *




def reference2array(path_file):

    """Reads the hyperspectral image and converts it to array, reads the metadata and extracts the wavelength

    Inputs:
    path_file      = path to the reference file

    Returns:
    reference_array_ave = reference in array format


    :param path_file: str
    :return reference_array_ave: numpy.ndarray

    """
    params.device += 1

    if os.path.isfile(path_file) == False:
        fatal_error(str(path_file) + " does not exist")

    if path_file is None:
        fatal_error("Failed to open " + path_file)

    # reads hyperspectral data
    gdalreference = gdal.Open(path_file)

    # converts hyperspectral data to array
    #reference_array = gdalreference.ReadAsArray()

    # extracts shape of the array
    cols = gdalreference.RasterXSize
    rows = gdalreference.RasterYSize
    bands = gdalreference.RasterCount

    output_list = []
    for i in range(1,bands+1):
        band = gdalreference.GetRasterBand(i)
        reference_array = band.ReadAsArray(0, 0, cols, rows)
        for y in zip(*reference_array):
            avg_reflectance = sum(y)/len(y)
            #print (avg_reflectance)
            (output_list.append( (avg_reflectance) ))
            #print (output_list)
    reference_array_ave = np.reshape(output_list, (bands, cols))

    return reference_array_ave
