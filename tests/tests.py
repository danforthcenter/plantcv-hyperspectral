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

def test_fake_test():
    assert 5 == 5
# ##############################
# Clean up test files
# ##############################
def teardown_function():
    shutil.rmtree(TEST_TMPDIR)
