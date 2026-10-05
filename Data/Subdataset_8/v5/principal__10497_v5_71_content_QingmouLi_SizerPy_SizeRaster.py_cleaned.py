
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
def main():
    args = sp.RasterParser()
    inRasterObj = sp.SizeRaster(args.inputRaster)
    inRasterObj.SizeBands(args.outRaster, factor=args.factor, d1Interpolate=args.d1Interpolate)
    print('Resizing completed.')
if __name__ == '__main__':
    main()
