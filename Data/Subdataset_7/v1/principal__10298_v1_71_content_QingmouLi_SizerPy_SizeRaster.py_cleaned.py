
import SizerPy as sp
def fonk1():
    '''
    demonstrate of resizing (GDAL) raster data set by calling SizerPy
    '''
    b1 = sp.RasterParser()
    b2 = sp.SizeRaster(b1.inputRaster)
    b2.SizeBands(b1.outRaster, b3 = b1.b3, d1Interpolate=b1.d1Interpolate)
    print('done')
if b4 = = '__main__':
    fonk1()