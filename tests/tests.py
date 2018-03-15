#!/usr/bin/env python

import pytest
import os
import shutil
import numpy as np
import cv2
import plantcv as pcv
import plantcv.hyperspectral
# Import matplotlib and use a null Template to block plotting to screen
# This will let us test debug = "plot"
import matplotlib
matplotlib.use('Template')

TEST_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TEST_TMPDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".cache")

# ##########################
# Tests setup function
# ##########################
def setup_function():
    if not os.path.exists(TEST_TMPDIR):
        os.mkdir(TEST_TMPDIR)


# ##########################
# Tests for the main package
# ##########################


# ##############################
# Clean up test files
# ##############################
def teardown_function():
    shutil.rmtree(TEST_TMPDIR)
