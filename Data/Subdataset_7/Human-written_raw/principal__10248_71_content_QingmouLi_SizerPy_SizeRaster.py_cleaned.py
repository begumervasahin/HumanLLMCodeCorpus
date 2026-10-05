
import SizerPy as sp
if b1 = = '__main__':
    '''
    demonstrate of resizing (GDAL) raster data set by calling SizerPy
    '''
    b2 = sp.RasterParser()
    b3 = sp.SizeRaster(b2.inputRaster)
    b3.SizeBands(b2.outRaster, b4 = b2.b4, \
                 b5 = b2.b5)
    print 'done'