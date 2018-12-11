from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
import os
from spectral import *
from osgeo import gdal
from osgeo.gdalconst import *
import numpy as np

def reference2array(path):
    """this function allows you read in hyperspectral reference in raw format and returns it as array that is averaged
    (this will be used to normalize the raw hyperspectral image)
    Inputs:
    path     = path to the raw file of reference

    Returns:
    image_array_all = hyperspectral reference image in array format
    gdalhyper = hyperspectral reference image
    pixelWidth = pixelWidth
    cols = number of cols of raw image
    rows = number of rows of raw image
    bands = number of bands of raw image


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
        print ("Couldn't open this file: " + path)
        sys.exit("Try again!")
    else:
        print ("%s opened successfully" %path)
        print ('Get image size')
        cols = gdalhyper.RasterXSize
        rows = gdalhyper.RasterYSize
        bands = gdalhyper.RasterCount
        print ("columns: %i" %cols)
        print ("rows: %i" %rows)
        print ("bands: %i" %bands)
        print ('Get georeference information')
        geotransform = gdalhyper.GetGeoTransform()
        originX = geotransform[0]
        originY = geotransform[3]
        pixelWidth = geotransform[1]
        pixelHeight = geotransform[5]
        print ("origin x: %i" %originX)
        print ("origin y: %i" %originY)
        print ("width: %2.2f" %pixelWidth)
        print ("height: %2.2f" %pixelHeight)
        # Set pixel offset.....
        print ('Convert image to 2D array')
        band = gdalhyper.GetRasterBand(1)
        image_array = band.ReadAsArray(0, 0, cols, rows)
        image_array_name = path
        print (type(image_array))
        print (image_array.shape)
    output_list = []
    for i in range(1,bands+1):
        band = gdalhyper.GetRasterBand(i)
        image_array = band.ReadAsArray(0, 0, cols, rows)
        for y in zip(*image_array):
            avg_reflectance = sum(y)/len(y)
            #print (avg_reflectance)
            (output_list.append( (avg_reflectance) ))
            #print (output_list)
    image_array_ave = np.reshape(output_list, (bands, cols))
    print ('Average image width')
    print (image_array_ave.shape)

    return image_array_all, gdalhyper, cols, rows, bands
