import SizerPy as sp
def fonk1():
    b1 = sp.RasterParser()
    b2 = b1.inputRaster
    b3 = b1.outRaster
    b4 = b1.b7
    b5 = b1.d1Interpolate
    b6 = sp.SizeRaster(b2)
    b6.SizeBands(b3, b7 = b4, d1Interpolate=b5)
    print('Resizing of raster bands completed.')
if b8 = = '__main__':
    fonk1()