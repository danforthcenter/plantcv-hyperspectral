## Converting hyperspectral to array

To read hyperspectral image and convert it to array, a path to the hyperspectral image is used.

**hs2array**(*path_file, path_wl*)

**returns** image_array, cols, rows, bands, wavelength

- **Parameters:**
    - path_file - path to the hyperspectral file including the name of the file
    - path_wl - path to the metadata containing wavelength

- **Context:**
    - This function was written to convert hyperspectral image to array to work with reflectance values.

```python

from plantcv import plantcv.hyperspectral as hyp

image_array, cols, rows, bands, wavelength = hs2array(path_file, path_wl)

```
