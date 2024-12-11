
'''
This code follows the terms of GPLv2.
Disclaimer: The authors permit the usage of this code in research and applications,
            but make no guarantees or implicit claims of its accuracy. Users are
            encouraged to independently verify its results.
References:
    Li, Q. and Delher S. A. 2018. SizerPy: a Python tool for resizing raster
        data by interpolation in the eigenspace, Computers & geosciences, xxx,
        p. xx-xx
    Li, Q. and Dehler S. A. 2015. Inverse Spatial principal component analysis
        for geophysical data interpolation. Journal of Applied Geophysics, 115,
        p.79-91.
Authors:
    Qingmou Li and Sonya A. Dehler
    Natural Resources of Canada
    Qingmou.Li@Canada.ca
    sonya.dehler@canada.ca
'''
import SizerPy as sp
def fonk1():
    b1 = sp.RasterParser()
    b2 = sp.SizeRaster(b1.inputRaster)
    b2.SizeBands(b1.outRaster, b3 = b1.b3, d1Interpolate=b1.d1Interpolate)
    print('Resizing completed.')
if b4 = = '__main__':
    fonk1()
