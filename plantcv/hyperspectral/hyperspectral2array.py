import os
from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
import os
from spectral import *
from osgeo import gdal
from osgeo import gdalconst
from osgeo.gdalconst import *
import numpy as np

def read_hyperspectral_as_array(path):
    """this function allows you read in hyperspectral images in raw format as array (needs associated .hdr file)

    Inputs:
    path     = path to .hdr file, there is the assumption that .hdr file name matches raw image name

    Returns:
    z = average image
    gdalhyper = hyperspectral image
    immage_array = averag of hyperspectral image as array
    pixelWidth =
    cols = number of cols
    rows = number of rows
    bands = number of bands


    :param hyperimg: spectral object
    :param bands: list of band centers
    :param path: string
    :return filname: string
    """

    device += 1

    if path.endswith("_raw") == False:
        fatal_error("Input is not an bil file")
    if os.path.isfile(path) == False:
        fatal_error(str(path) + " does not exist")

    gdalhyper = gdal.Open(path, GA_ReadOnly)
    if gdalhyper is None:
        print("Couldn't open this file: " + path)
        sys.exit("Try again!")
    else:
        print("%s opened successfully" % path)
        print('Get image size')
        cols = gdalhyper.RasterXSize
        rows = gdalhyper.RasterYSize
        bands = gdalhyper.RasterCount
        print("columns: %i" % cols)
        print("rows: %i" % rows)
        print("bands: %i" % bands)
        print('Get georeference information')
        geotransform = gdalhyper.GetGeoTransform()
        originX = geotransform[0]
        originY = geotransform[3]
        pixelWidth = geotransform[1]
        pixelHeight = geotransform[5]
        print("origin x: %i" % originX)
        print("origin y: %i" % originY)
        print("width: %2.2f" % pixelWidth)
        print("height: %2.2f" % pixelHeight)
        # Set pixel offset.....
        print('Convert image to 2D array')
        band = gdalhyper.GetRasterBand(1)
        image_array = band.ReadAsArray(0, 0, cols, rows)
        image_array_name = path
        print(type(image_array))
        print(image_array.shape)
    output_list = np.zeros((bands, rows, cols), dtype=np.float32)
    for i in range(1, bands):
        band = gdalhyper.GetRasterBand(i)
        image_array3 = band.ReadAsArray(0, 0, cols, rows)
        image_array_name = path
        output_list[i] = image_array
    image_array_all = np.reshape(output_list, (bands, rows, cols))
    print('full image array')
    print(image_array_all.shape)

    return image_array_all, gdalhyper, pixelWidth, cols, rows, bands
