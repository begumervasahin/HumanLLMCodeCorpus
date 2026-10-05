
import SizerPy as sp
def main():
    args = sp.RasterParser()
    input_raster = args.inputRaster
    out_raster = args.outRaster
    factor = args.factor
    d1_interpolate = args.d1Interpolate
    raster_object = sp.SizeRaster(input_raster)
    raster_object.SizeBands(out_raster, factor=factor, d1Interpolate=d1_interpolate)
    print('Resizing of raster bands completed.')
if __name__ == '__main__':
    main()