import time
import os
import arcpy
import autoLin
def main():
    start_time = time.strftime("%m%d_%H%M%S")
    print("Process started at:", start_time)
    arcpy.CheckOutExtension("3D")
    print("arcpy module imported at:", time.strftime("%m%d_%H%M%S"))
    arcpy.env.overwriteOutput = True
    terrain = r"D:\Kuba\PhD_data\Thesis\AutoLin\Zdroje\Mentlik\Srni\DMR.gdb\Prasily\Prasily_Terrain"
    resolutions = range(10, 11, 5)
    outDEMmask = r"d:\Kuba\PhD_data\Thesis\AutoLin\DEM\Prasily\LLS\pr_lls_dem_"
    for cell_size in resolutions:
        outDEM = outDEMmask + str(cell_size)
        if not os.path.exists(outDEM):
            tempDEM = os.path.join(autoLin.getDir(outDEM), "tempDEM")
            if not os.path.exists(tempDEM):
                arcpy.TerrainToRaster_3d(terrain, tempDEM, "FLOAT", "LINEAR", f"CELLSIZE {cell_size}", "0")
            try:
                print("Filling DEM at:", time.strftime("%m%d_%H%M%S"), ":", outDEM)
                arcpy.gp.Fill_sa(tempDEM, outDEM)
            except:
                print("Failed to fill DEM:", outDEM, "- Continuing with the next one")
                autoLin.deletePath(tempDEM)
                continue
            autoLin.deletePath(tempDEM)
        else:
            print("Skipping existing DEM:", outDEM)
if __name__ == "__main__":
    main()