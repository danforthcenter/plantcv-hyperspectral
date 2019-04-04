## Converting reference image to 2D array

If the hyperspectral image was not calibrated, this functions reads reference image (white reference or dark reference) to calibrate with plantcv.hyperspectral function calibrate_hs.

**reference2array**(*path_file*)

**returns** reference_array_ave

- **Parameters:**
    - path_file - path to the reference file including the name of the file

- **Context:**
    - This function was written to convert reference image to a 2D array to work with reflectance values.

```python

from plantcv import plantcv.hyperspectral as hyp

reference_array_ave = reference2array(path_file)

```
