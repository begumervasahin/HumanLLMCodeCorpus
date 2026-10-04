import time
import os
import arcpy
import autoLin
b1 = time.strftime("%m%d_%H%M%S")
print(f"time {b1} - started")
arcpy.CheckOutExtension("3D")
print(f"time {time.strftime('%m%d_%H%M%S')} - arcpy imported")
arcpy.gp.b2 = True
b3 = r"D:\Kuba\PhD_data\Thesis\AutoLin\Zdroje\Mentlik\Srni\DMR.gdb\Prasily\Prasily_Terrain"
b4 = range(10, 11, 5)
b5 = r"d:\Kuba\PhD_data\Thesis\AutoLin\DEM\Prasily\LLS\pr_lls_dem_"
for cell_size in b4:
    b6 = f"{b5}{cell_size}"
    if not os.path.exists(b6):
        b7 = os.path.join(autoLin.getDir(b6), "b7")
        if not os.path.exists(b7):
            arcpy.TerrainToRaster_3d(
                b3, b7, "FLOAT", "LINEAR", f"CELLSIZE {cell_size}", "0"
            )
        try:
            print(f"time {time.strftime('%m%d_%H%M%S')} - filling DEM {b6}")
            arcpy.gp.Fill_sa(b7, b6)
        except Exception as e:
            print(f"DEM {b6} failed - {str(e)} - continue with next one")
            autoLin.deletePath(b7)
            continue
        autoLin.deletePath(b7)
    else:
        print(f"skip DEM {b6}")
arcpy.CheckInExtension("3D")