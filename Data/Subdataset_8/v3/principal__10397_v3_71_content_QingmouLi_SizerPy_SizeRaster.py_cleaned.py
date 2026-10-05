import SizerPy as sp
def resize_raster():
    args = sp.RasterParser()
    input_raster = args.inputRaster
    out_raster = args.outRaster
    resizing_factor = args.factor
    interpolation_method = args.d1Interpolate
    raster_resizer = sp.SizeRaster(input_raster)
    raster_resizer.SizeBands(out_raster, factor=resizing_factor, d1Interpolate=interpolation_method)
    print('Resizing of raster bands completed.')
if __name__ == '__main__':
    resize_raster()