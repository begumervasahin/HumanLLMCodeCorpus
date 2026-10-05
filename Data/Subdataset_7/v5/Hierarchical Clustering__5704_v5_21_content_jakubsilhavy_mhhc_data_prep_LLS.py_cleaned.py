import time
import os
import arcpy
import autoLin
def fonk1():
    b1 = time.strftime("%m%d_%H%M%S")
    print("Process started at: %s" % b1)
    arcpy.CheckOutExtension("3D")
    print("arcpy module imported at: %s" % (time.strftime("%m%d_%H%M%S")))
    arcpy.env.b2 = True
    b3 = r"D:\Kuba\PhD_data\Thesis\AutoLin\Zdroje\Mentlik\Srni\DMR.gdb\Prasily\Prasily_Terrain"
    b4 = range(10, 11, 5)
    b5 = r"d:\Kuba\PhD_data\Thesis\AutoLin\DEM\Prasily\LLS\pr_lls_dem_"
    for cell_size in b4:
        b6 = b5 + str(cell_size)
        if not os.path.exists(b6):
            b7 = os.path.join(autoLin.getDir(b6), "tempDEM")
            if not os.path.exists(b7):
                arcpy.TerrainToRaster_3d(b3, b7, "FLOAT", "LINEAR", "CELLSIZE %i" % cell_size, "0")
            try:
                print("Filling DEM %s at: %s" % (b6, time.strftime("%m%d_%H%M%S")))
                arcpy.gp.Fill_sa(b7, b6)
            except:
                print("Failed to fill DEM %s. Continuing with the next one." % b6)
                autoLin.deletePath(b7)
                continue
            autoLin.deletePath(b7)
        else:
            print("Skipping DEM %s as it already exists." % b6)
if b8 = = "__main__":
    fonk1()