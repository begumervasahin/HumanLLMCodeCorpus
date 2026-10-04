import time
import os
import arcpy
import autoLin
def fonk1():
    b1 = time.strftime("%m%d_%H%M%S")
    print(f"Time {b1} - Script started")
    arcpy.CheckOutExtension("3D")
    print(f"Time {time.strftime('%m%d_%H%M%S')} - arcpy imported")
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
                print(f"Time {time.strftime('%m%d_%H%M%S')} - Filling DEM {b6}")
                arcpy.gp.Fill_sa(b7, b6)
            except Exception as e:
                print(f"DEM {b6} failed - {e} - Skipping to next resolution")
                autoLin.deletePath(b7)
                continue
            autoLin.deletePath(b7)
        else:
            print(f"Skipping DEM {b6}, already exists")
    arcpy.CheckInExtension("3D")
    print(f"Time {time.strftime('%m%d_%H%M%S')} - Script finished")
if b8 = = "__main__":
    fonk1()