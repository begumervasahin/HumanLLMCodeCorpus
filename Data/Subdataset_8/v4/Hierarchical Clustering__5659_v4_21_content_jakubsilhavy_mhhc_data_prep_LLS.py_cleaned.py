import time
import os
import arcpy
import autoLin
start_time = time.strftime("%m%d_%H%M%S")
print("Time %s - Process started" % start_time)
arcpy.CheckOutExtension("3D")
print("Time %s - arcpy module imported" % (time.strftime("%m%d_%H%M%S")))
arcpy.gp.overwriteOutput = True
terrain = r"D:\Kuba\PhD_data\Thesis\AutoLin\Zdroje\Mentlik\Srni\DMR.gdb\Prasily\Prasily_Terrain"
resolutions = range(10, 11, 5)
outDEMmask = r"d:\Kuba\PhD_data\Thesis\AutoLin\DEM\Prasily\LLS\pr_lls_dem_"
for cell_size in resolutions:
    outDEM = outDEMmask + "%i" % cell_size
    if not os.path.exists(outDEM):
        tempDEM = autoLin.getDir(outDEM) + "tempDEM"
        if not os.path.exists(tempDEM):
            arcpy.TerrainToRaster_3d(terrain, tempDEM, "FLOAT", "LINEAR", "CELLSIZE %i" % cell_size, "0")
        try:
            print("Time %s - Filling DEM %s" % (time.strftime("%m%d_%H%M%S"), outDEM))
            arcpy.gp.Fill_sa(tempDEM, outDEM)
        except:
            print("DEM %s failed - continue with next one" % outDEM)
            autoLin.deletePath(tempDEM)
            continue
        autoLin.deletePath(tempDEM)
    else:
        print("Skip DEM %s" % outDEM)