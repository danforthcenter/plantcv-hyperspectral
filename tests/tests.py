#!/usr/bin/env python

import pytest
import os
import shutil
import numpy as np
import cv2
import plantcv as pcv
import plantcv.hyperspectral as hy
# Import matplotlib and use a null Template to block plotting to screen
# This will let us test debug = "plot"
import matplotlib
matplotlib.use('Template', warn=False)

TEST_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TEST_TMPDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".cache")

TEST_INPUT_HYPER = "darkReference.hdr"
TEST_SPICE = "spice_data.npz"

# ##########################
# Tests setup function
# ##########################
def setup_function():
    if not os.path.exists(TEST_TMPDIR):
        os.mkdir(TEST_TMPDIR)


# ##########################
# Tests for the main package
# ##########################

def test_read_hyperspectral():
    hyperimg, bands, path, filename = hy.read_hyperspectral(os.path.join(TEST_DATA, TEST_INPUT_HYPER))
    assert len(bands) == 978


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
    params = hy.SPICE.SPICEParameters()
    params.initEM = init_endmem
    params.produceDisplay = 0
    # Run the algorithm
    endm, P = hy.SPICE.SPICE(input_data, params)
    # assert with a 0.01% tolerance, since the values are floats (can't do exact comparison)
    assert np.allclose(endm, final_endmem, rtol=0.0001) and np.allclose(P, final_prop, rtol=0.0001)


# ##############################
# Clean up test files
# ##############################
def teardown_function():
    shutil.rmtree(TEST_TMPDIR)
