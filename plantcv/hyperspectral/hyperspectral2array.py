from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
import os
from spectral import *
from osgeo import gdal
from osgeo.gdalconst import *
import numpy as np
from matplotlib import pyplot as plt



def hyperspectral2array(path):
    """this function allows you read in hyperspectral images in raw or corrected format and returns it as array as well as a sample image from the bandnumber entered (array shape: No.
    of bands, image width, image length)

    Inputs:
    path     = path to the hyperspectral file

    Returns:
    image_array_all = hyperspectral image in array format
    gdalhyper = hyperspectral image
    plots a sample image from the entered waveband


    :param hyperimg: spectral object
    :param bands: list of band centers
    :param path: string
    :return filname: string
    """

    params.device += 1


    if os.path.isfile(path) == False:
        fatal_error(str(path) + " does not exist")

    gdalhyper = gdal.Open(path, GA_ReadOnly)
    if gdalhyper is None:
        print("Couldn't open this file: " + path)
        sys.exit("Try again!")
    else:
        print("%s opened successfully" % path)
        gdalhyper = gdal.Open(path)
        arrhyper = gdalhyper.ReadAsArray()
        cols = gdalhyper.RasterXSize
        rows = gdalhyper.RasterYSize
        bands = gdalhyper.RasterCount
        print("columns: %i" % cols)
        print("rows: %i" % rows)
        print("bands: %i" % bands)
        print('Get georeference information')
        hyper_array = np.transpose(arrhyper[:,:,:], (2,1,0))
            print('array shape')
        print(hyper_array.shape)
        print('sample image from band')
        hyper_array_plt = hyper_array[:,:,band]
        plt.imshow(hyper_array_plt)


    return hyper_array, gdalhyper
