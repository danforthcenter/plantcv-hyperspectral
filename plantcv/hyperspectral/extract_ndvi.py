# extract any channel from the hyperspectral array

import numpy as np
from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
import matplotlib.pyplot as plt



"""Reads the hyperspectral image and converts it to array, reads the metadata and extracts the wavelength

    Inputs:
    image_array = mage in array forma
    wavelength = wavelengths in list

    Returns:
    img2 = ndvi using the average value of reflectance in red and nir channels

    :param a: int
    :param b: int
    :return channelsum: numpy.ndarray 
    

    """
    params.device += 1

def ndvi (image_array, wavelength):


    if array is None:
        fatal_error("Failed to open " + array)

    #extract red channel
    rwl = [i for i in wavelength if i>=663 and i<=673]
    indrwl = []
    for i in rwl:
        c = wavelength.index(i)
        (indrwl.append( (c) ))
    red1 = image_array[indrwl[0]:indrwl[-1]]
    rsum = np.sum(red1, axis=0)
    #extract NIR channel
    nir = [i for i in wavelength if i>=820 and i<=860]
    indnir = []
    for i in nir:
        b = wavelength.index(i)
        (indnir.append( (b) ))
    nir1 = image_array[indnir[0]:indnir[-1]]
    nirsum = np.sum(nir1, axis=0)

    #create ndvi
    imgnum = nirsum - rsum
    imgden = nirsum + rsum
    imgndvi = imgnum / imgden

    #plot ndvi
    maxno1 = np.max(imgndvi) # Get the information of the incoming image type
    data1ndvi = imgndvi.astype(np.float64) / maxno1 # normalize the data to 0 - 1
    data2ndvi = 255 * data1ndvi # Now scale by 255
    img2 = data2ndvi.astype(np.uint8)
    #imag2_pseducolor = pseudocolor(gray_img=img2, mask=None, cmap='plasma', background="white", min_value=0, max_value=255, obj=None, dpi=None,
                  # axes=True, colorbar=True, path=".")

    # plot or print the image
    if params.debug == 'print':
        plt.imsave(os.path.join(params.debug_outdir, str(params.device) + '_ndvi' + '.png'), img2)
    elif params.debug == 'plot':
        plt.imshow(img2, cmap='gray')
    return img2
