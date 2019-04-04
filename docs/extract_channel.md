## Extracting any channel from hyperspectral image

To read hyperspectral image and convert it to array, a path to the hyperspectral image is used.

**extract_channel**(*a, b, image_array, wavelength*)

**returns** channelsum

- **Parameters:**
    - image_array - hyperspectral image that is converted to array with plantcv.hyperspectral function hs2array
    - wavelength - wavelength list that is extracted with plantcv.hyperspectral function hs2array
    - a - lower range of wavelength to extract
    - b - higher range of wavelength to extract

- **Context:**
    - This function was written to extract any channel to visualize or to use for creating vegetation indices.

```python

from plantcv import plantcv.hyperspectral as hyp

# Set global debug behavior to None (default), "print" (to file), or "plot"
pcv.params.debug = "print"

channelsum = extract_ndvi(a, b, image_array, wavelength)

```
