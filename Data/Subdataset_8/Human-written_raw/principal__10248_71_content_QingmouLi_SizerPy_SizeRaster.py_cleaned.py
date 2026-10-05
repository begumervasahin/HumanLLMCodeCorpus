
import SizerPy as sp
if __name__ == '__main__':
    '''
    demonstrate of resizing (GDAL) raster data set by calling SizerPy
    '''
    args=sp.RasterParser()
    inRasterObj = sp.SizeRaster(args.inputRaster)
    inRasterObj.SizeBands(args.outRaster, factor=args.factor, \
                 d1Interpolate = args.d1Interpolate)
    print 'done'