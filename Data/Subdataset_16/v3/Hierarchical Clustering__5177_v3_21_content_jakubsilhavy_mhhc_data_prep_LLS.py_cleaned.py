import time
import os
import arcpy
import autoLin
def fonk1(message):
    b1 = time.strftime("%m%d_%H%M%S")
    print(f"Time {b1} - {message}")
def fonk2(b4, b2, cell_size):
    arcpy.TerrainToRaster_3d(
        b4, b2, "FLOAT", "LINEAR", f"CELLSIZE {cell_size}", "0"
    )
def fonk3(b2, b7):
    arcpy.gp.Fill_sa(b2, b7)
def fonk4(b4, b7, cell_size):
    b2 = os.path.join(autoLin.getDir(b7), "tempDEM")
    if not os.path.exists(b2):
        fonk2(b4, b2, cell_size)
    try:
        fonk1(f"Filling DEM {b7}")
        fonk3(b2, b7)
    except Exception as e:
        fonk1(f"DEM {b7} failed - {e} - Skipping to next resolution")
        autoLin.deletePath(b2)
        return
    autoLin.deletePath(b2)
def fonk5():
    fonk1("Script started")
    arcpy.CheckOutExtension("3D")
    fonk1("arcpy imported")
    arcpy.gp.b3 = True
    b4 = r"D:\Kuba\PhD_data\Thesis\AutoLin\Zdroje\Mentlik\Srni\DMR.gdb\Prasily\Prasily_Terrain"
    b5 = range(10, 11, 5)
    b6 = r"d:\Kuba\PhD_data\Thesis\AutoLin\DEM\Prasily\LLS\pr_lls_dem_"
    for cell_size in b5:
        b7 = f"{b6}{cell_size}"
        if not os.path.exists(b7):
            fonk4(b4, b7, cell_size)
        else:
            fonk1(f"Skipping DEM {b7}, already exists")
    arcpy.CheckInExtension("3D")
    fonk1("Script finished")
if b8 = = "__main__":
    fonk5()