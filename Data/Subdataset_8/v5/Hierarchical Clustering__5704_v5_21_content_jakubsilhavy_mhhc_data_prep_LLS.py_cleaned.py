import time
import os
import arcpy
import autoLin
def main():
    start_time = time.strftime("%m%d_%H%M%S")
    print("Process started at: %s" % start_time)
    arcpy.CheckOutExtension("3D")
    print("arcpy module imported at: %s" % (time.strftime("%m%d_%H%M%S")))
    arcpy.env.overwriteOutput = True
    terrain = r"D:\Kuba\PhD_data\Thesis\AutoLin\Zdroje\Mentlik\Srni\DMR.gdb\Prasily\Prasily_Terrain"
    resolutions = range(10, 11, 5)
    out_dem_mask = r"d:\Kuba\PhD_data\Thesis\AutoLin\DEM\Prasily\LLS\pr_lls_dem_"
    for cell_size in resolutions:
        out_dem = out_dem_mask + str(cell_size)
        if not os.path.exists(out_dem):
            temp_dem = os.path.join(autoLin.getDir(out_dem), "tempDEM")
            if not os.path.exists(temp_dem):
                arcpy.TerrainToRaster_3d(terrain, temp_dem, "FLOAT", "LINEAR", "CELLSIZE %i" % cell_size, "0")
            try:
                print("Filling DEM %s at: %s" % (out_dem, time.strftime("%m%d_%H%M%S")))
                arcpy.gp.Fill_sa(temp_dem, out_dem)
            except:
                print("Failed to fill DEM %s. Continuing with the next one." % out_dem)
                autoLin.deletePath(temp_dem)
                continue
            autoLin.deletePath(temp_dem)
        else:
            print("Skipping DEM %s as it already exists." % out_dem)
if __name__ == "__main__":
    main()