import time
import os
import arcpy
import autoLin
start_time = time.strftime("%m%d_%H%M%S")
print(f"time {start_time} - started")
arcpy.CheckOutExtension("3D")
print(f"time {time.strftime('%m%d_%H%M%S')} - arcpy imported")
arcpy.gp.overwriteOutput = True
terrain = r"D:\Kuba\PhD_data\Thesis\AutoLin\Zdroje\Mentlik\Srni\DMR.gdb\Prasily\Prasily_Terrain"
resolutions = range(10, 11, 5)
outDEMmask = r"d:\Kuba\PhD_data\Thesis\AutoLin\DEM\Prasily\LLS\pr_lls_dem_"
for cell_size in resolutions:
    outDEM = f"{outDEMmask}{cell_size}"
    if not os.path.exists(outDEM):
        tempDEM = os.path.join(autoLin.getDir(outDEM), "tempDEM")
        if not os.path.exists(tempDEM):
            arcpy.TerrainToRaster_3d(
                terrain, tempDEM, "FLOAT", "LINEAR", f"CELLSIZE {cell_size}", "0"
            )
        try:
            print(f"time {time.strftime('%m%d_%H%M%S')} - filling DEM {outDEM}")
            arcpy.gp.Fill_sa(tempDEM, outDEM)
        except Exception as e:
            print(f"DEM {outDEM} failed - {str(e)} - continue with next one")
            autoLin.deletePath(tempDEM)
            continue
        autoLin.deletePath(tempDEM)
    else:
        print(f"skip DEM {outDEM}")
arcpy.CheckInExtension("3D")