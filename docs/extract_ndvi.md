## Extracting NDVI from hyperspectral image

To read hyperspectral image and extract normalized difference vegetation index (NDVI), the array format of the hyperspectral image is used.

**extract_channel**(*image_array, wavelength*)

**returns** imgndvi2

- **Parameters:**
    - image_array - hyperspectral image that is converted to array with plantcv.hyperspectral function hs2array
    - wavelength - wavelength list that is extracted with plantcv.hyperspectral function hs2array

- **Context:**
    - This function was written to extract ndvi to use as threshold for separating plant from background.

```python

from plantcv import plantcv.hyperspectral as hyp

# Set global debug behavior to None (default), "print" (to file), or "plot"
pcv.params.debug = "print"

imgndvi2 = extract_ndvi(image_array, wavelength)

```
