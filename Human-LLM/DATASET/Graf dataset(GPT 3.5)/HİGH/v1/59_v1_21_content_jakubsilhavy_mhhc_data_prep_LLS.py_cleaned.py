import time
import os
import arcpy
import autoLin
b1 = time.strftime("%m%d_%H%M%S")
print("time %s - started" % (b1))
arcpy.CheckOutExtension("3D")
print("time %s - arcpy imported" % (time.strftime("%m%d_%H%M%S")))
arcpy.env.b2 = True
b3 = r"D:\Kuba\PhD_data\Thesis\AutoLin\Zdroje\Mentlik\Srni\DMR.gdb\Prasily\Prasily_Terrain"
b4 = range(10, 11, 5)
b5 = r"d:\Kuba\PhD_data\Thesis\AutoLin\DEM\Prasily\LLS\pr_lls_dem_"
for cellSize in b4:
    b6 = b5 + "%i" % cellSize
    if not os.path.exists(b6):
        b7 = autoLin.getDir(b6) + "b7"
        if not os.path.exists(b7):
            arcpy.TerrainToRaster_3d(b3, b7, "FLOAT", "LINEAR", "CELLSIZE %i" % cellSize, "0")
        try:
            print("time %s - filling DEM %s" % (time.strftime("%m%d_%H%M%S"), b6))
            arcpy.gp.Fill_sa(b7, b6)
        except:
            print("DEM %s failed - continue with next one" % b6)
            autoLin.deletePath(b7)
            continue
        autoLin.deletePath(b7)
    else:
        print("skip DEM %s" % b6)