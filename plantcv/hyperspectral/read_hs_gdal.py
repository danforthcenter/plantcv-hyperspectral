import os
from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
from osgeo import gdal

def read_hs_gdal(path):
    """this function allows you read in hyperspectral images in raw format

    Inputs:
    path     = path to hyperspectral bil file

    Returns:
    hyperimge = image mask
    wavelength = band centers
    filename = name of hyperspectral image

    :param path: string
    :return hyperimg: spectral.io.bilfile.BilFile
    :return wavelength: list
    :return filname: str
    """

    params.device += 1

    if os.path.isfile(path) == False:
        fatal_error(str(path) + " does not exist")

    gdalhyper = gdal.Open(path)
    wavelength = gdalhyper.GetRasterBand(1)
    bandNo = gdalhyper.RasterCount
    if params.debug == "plot":
        message = "_input_image.png" + " successfully opened. With a total of " + str(
            bandNo) + " bands."
        print(message)

    return gdalhyper, wavelength
