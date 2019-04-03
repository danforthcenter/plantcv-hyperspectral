import os
from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
from osgeo import gdal
import rasterio

def read_hyperspectral_gdal(path):
    """this function allows you read in hyperspectral images in raw format

    Inputs:
    path     = path to hyperspectral bil file

    Returns:
    hyperimge = image mask
    bands = band centers
    path = path to hyperspectral image
    filename = name of hyperspectral image

    :param hyperimg: spectral object
    :param bands: list of band centers
    :param path: string
    :return filname: string
    """

    params.device += 1

    if os.path.isfile(path) == False:
        fatal_error(str(path) + " does not exist")

    path1, filename = os.path.split(path)
    gdalhyper = gdal.open(path)
    bands = gdalhyper.GetRasterBand(1)
    bandNo = gdalhyper.RasterCount
    print("Band Type={}".format(gdal.GetDataTypeName(bands.DataType)))

    if params.debug == "print":
        message = str(filename) + "_input_image.png" + " succesfully opened. With a total of " + str(
            bandNo) + " bands."
        print(message)
    elif params.debug == "plot":
        message = str(filename) + "_input_image.png" + " succesfully opened. With a total of " + str(
            bandNo) + " bands."
        print(message)

    return hyperimg, bands, path, filename
