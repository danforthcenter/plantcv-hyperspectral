
#!/usr/bin/env python

import pytest
import os
import shutil
import numpy as np
import cv2
import plantcv as pcv
from plantcv import hyperspectral as hyp
from plantcv import plantcv as pcv
# Import matplotlib and use a null Template to block plotting to screen
# This will let us test debug = "plot"
import matplotlib

matplotlib.use('Template', warn=False)

TEST_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TEST_TMPDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".cache")
TEST_INPUT_HYPER = "data"
TEST_INPUT_META = "data.hdr"
TEST_INPUT_HYPER_ARRAY = "image_array.npz"
TEST_INPUT_WL = "wavelength.npz"
TEST_INPUT_DARK = "darkReference"
TEST_INPUT_WHITE = "whiteReference"
TEST_INPUT_RAW = "raw"
TEST_INPUT_WHITE_REFERENCE = "reference_array_white.npz"
TEST_INPUT_DARK_REFERENCE = "reference_array_dark.npz"
TEST_SPICE = "spice_data.npz"

#TEST_SPICE = "spice_data.npz"



# ##########################
# Tests setup function
# ##########################
def setup_function():
    if not os.path.exists(TEST_TMPDIR):
        os.mkdir(TEST_TMPDIR)



# ##########################
# Tests for the main package
# ##########################

def test_hs2array():

    image_array, cols, rows, bands, wavelength = hyp.hs2array(os.path.join(TEST_DATA, TEST_INPUT_HYPER),os.path.join(TEST_DATA, TEST_INPUT_META))
    assert bands == 148


def test_extract_channel():
    #read image_array
    image_array_npz = np.load(os.path.join(TEST_DATA, TEST_INPUT_HYPER_ARRAY), encoding="latin1")
    image_array = image_array_npz['arr_0']
    #read wavelength
    wavelength_npz = np.load(os.path.join(TEST_DATA, TEST_INPUT_WL), encoding="latin1")
    wavelength1 = wavelength_npz['arr_0']
    wavelength = wavelength1.tolist()

    channelsum = hyp.extract_channel(600, 650, image_array, wavelength)
    assert np.shape(channelsum) == (320, 445)

def test_extract_channel_plot():

    #read image_array
    image_array_npz = np.load(os.path.join(TEST_DATA, TEST_INPUT_HYPER_ARRAY), encoding="latin1")
    image_array = image_array_npz['arr_0']
    #read wavelength
    wavelength_npz = np.load(os.path.join(TEST_DATA, TEST_INPUT_WL), encoding="latin1")
    wavelength1 = wavelength_npz['arr_0']
    wavelength = wavelength1.tolist()
    # Test with debug = "print"
    pcv.params.debug = "print"
    _ = hyp.extract_channel(600, 650, image_array, wavelength)
    # Test with debug = "plot"
    pcv.params.debug = "plot"
    _ = hyp.extract_channel(600, 650, image_array, wavelength)
    # Test with debug = None
    pcv.params.debug = None
    channelsum = hyp.extract_channel(600, 650, image_array, wavelength)
    x, y, z = np.shape(image_array)
    x1, y1 = np.shape(channelsum)
    assert y == x1 and z == y1


def test_extract_ndvi():

    #read image_array
    image_array_npz = np.load(os.path.join(TEST_DATA, TEST_INPUT_HYPER_ARRAY), encoding="latin1")
    image_array = image_array_npz['arr_0']
    #read wavelength
    wavelength_npz = np.load(os.path.join(TEST_DATA, TEST_INPUT_WL), encoding="latin1")
    wavelength1 = wavelength_npz['arr_0']
    wavelength = wavelength1.tolist()

    img2 = hyp.extract_ndvi(image_array, wavelength)
    assert np.shape(img2) == (320, 445)

def test_extract_ndvi_plot():

    #read image_array
    image_array_npz = np.load(os.path.join(TEST_DATA, TEST_INPUT_HYPER_ARRAY), encoding="latin1")
    image_array = image_array_npz['arr_0']
    #read wavelength
    wavelength_npz = np.load(os.path.join(TEST_DATA, TEST_INPUT_WL), encoding="latin1")
    wavelength1 = wavelength_npz['arr_0']
    wavelength = wavelength1.tolist()
    # Test with debug = "print"
    pcv.params.debug = "print"
    _ = hyp.extract_ndvi(image_array, wavelength)
    # Test with debug = "plot"
    pcv.params.debug = "plot"
    _ = hyp.extract_ndvi(image_array, wavelength)
    # Test with debug = None
    pcv.params.debug = None
    img2 = hyp.extract_ndvi(image_array, wavelength)
    x, y, z = np.shape(image_array)
    x1, y1 = np.shape(img2)
    assert y == x1 and z == y1

def test_reference2array():

    reference_array_ave = hyp.reference2array(os.path.join(TEST_DATA, TEST_INPUT_DARK))
    assert np.shape(reference_array_ave) == (148, 320)

def test_calibrate_hs():

    #read image_array
    image_array_npz = np.load(os.path.join(TEST_DATA, TEST_INPUT_HYPER_ARRAY), encoding="latin1")
    image_array = image_array_npz['arr_0']

    #read white reference
    reference_array_white_npz = np.load(os.path.join(TEST_DATA, TEST_INPUT_WHITE_REFERENCE), encoding="latin1")
    reference_array_white = reference_array_white_npz['arr_0']

    #read dark reference
    reference_array_dark_npz = np.load(os.path.join(TEST_DATA, TEST_INPUT_DARK_REFERENCE), encoding="latin1")
    reference_array_dark = reference_array_dark_npz['arr_0']

    normz, one_channel = hyp.calibrate_hs(image_array, reference_array_white, reference_array_dark, 445, 320, 148)
    assert np.shape(normz) == (445, 320, 148)

def test_read_hs_gdal():

    gdalhyper, wavelength = hyp.read_hs_gdal(os.path.join(TEST_DATA, TEST_INPUT_HYPER))
    stats = wavelength.GetStatistics(True, True)
    stt1 = stats[1]

    assert stt1 == 1.5714285373688

def test_plantcv_spice_training():
    spice = np.load(os.path.join(TEST_DATA, TEST_SPICE))
    # In the SPICE algorithm, initialization parameters are randomized, these have a known output
    init_endmem = spice['init_endmembers']
    # Input data (HSI Image)
    input_data = spice['input_data']
    # Final data to test against
    final_endmem = spice['final_endmembers']
    final_prop = spice['final_proportions']
    # Load parameters, turn off display
    params = hyp.SPICE.SPICEParameters()
    params.initEM = init_endmem
    params.produceDisplay = 0
    # Run the algorithm
    endm, P = hyp.SPICE.SPICE(input_data, params)
    # assert with a 0.01% tolerance, since the values are floats (can't do exact comparison)
    assert np.allclose(endm, final_endmem, rtol=0.0001) and np.allclose(P, final_prop, rtol=0.0001)


# ##############################
# Clean up test files
# ##############################
def teardown_function():
    shutil.rmtree(TEST_TMPDIR)
