## Calibrating hyperspectral image

If the hyperspectral image was not calibrated, this functions reads in the hyperspectral image in array format as well as white and dark references and calibrates it.

**calibrate_hs**(*image_array, reference_array_white, reference_array_dark, rows, cols, bands*)

**returns** image_array, cols, rows, bands, wavelength

- **Parameters:**
    - image_array - image in array format that is generated form plantcv.hyperspectral function hs2array
    - reference_array_white - white reference data in array format that is generated from plantcv.hyperspectral function reference2array
    - reference_array_dark - dark reference data in array format that is generated from plantcv.hyperspectral function reference2array
    - cols = number of cols
    - rows = number of rows
    - bands = number of bands
    
- **Context:**
    - This function was written to calibrate a raw hyperspectral image and to show a sample image from the calibrated one.

```python

from plantcv import plantcv.hyperspectral as hyp

calibrated, sample_channel = calibrate_hs(image_array, reference_array_white, reference_array_dark, rows, cols, bands)

```
