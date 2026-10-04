import time
import os
import arcpy
import autoLin
def fonk1(message):
    b1 = time.strftime("%m%d_%H%M%S")
    print(f"Time {b1} - {message}")
def fonk2(b5, b2, cell_size):
    arcpy.TerrainToRaster_3d(
        b5, b2, "FLOAT", "LINEAR", f"CELLSIZE {cell_size}", "0"
    )
def fonk3(b2, b3):
    arcpy.gp.Fill_sa(b2, b3)
def fonk4(b5, b3, cell_size):
    b2 = os.path.join(autoLin.getDir(b3), "tempDEM")
    if not os.path.exists(b2):
        fonk2(b5, b2, cell_size)
    try:
        fonk1(f"Filling DEM {b3}")
        fonk3(b2, b3)
    except Exception as e:
        fonk1(f"DEM {b3} failed - {e} - Skipping to next resolution")
        autoLin.deletePath(b2)
        return
    autoLin.deletePath(b2)
def fonk5(b5, b6, b7):
    for cell_size in b7:
        b3 = f"{b6}{cell_size}"
        if not os.path.exists(b3):
            fonk4(b5, b3, cell_size)
        else:
            fonk1(f"Skipping DEM {b3}, already exists")
def fonk6():
    fonk1("Script started")
    try:
        arcpy.CheckOutExtension("3D")
        fonk1("arcpy imported")
        arcpy.gp.b4 = True
        b5 = r"D:\Kuba\PhD_data\Thesis\AutoLin\Zdroje\Mentlik\Srni\DMR.gdb\Prasily\Prasily_Terrain"
        b6 = r"d:\Kuba\PhD_data\Thesis\AutoLin\DEM\Prasily\LLS\pr_lls_dem_"
        b7 = range(10, 11, 5)
        fonk5(b5, b6, b7)
    finally:
        arcpy.CheckInExtension("3D")
        fonk1("Script finished")
if b8 = = "__main__":
    fonk6()