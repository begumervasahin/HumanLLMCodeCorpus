
'''
We adhere to the terms of GPLv2.
Disclaimer: Although authors permit the usage of this code in research and applications,
            there are no guarantees or implicit claims of its accuracy. Users are encouraged
            to verify its results independently.
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
if __name__ == '__main__':
    args = sp.RasterParser()
    inRasterObj = sp.SizeRaster(args.inputRaster)
    inRasterObj.SizeBands(args.outRaster, factor=args.factor, d1Interpolate=args.d1Interpolate)
    print('done')
