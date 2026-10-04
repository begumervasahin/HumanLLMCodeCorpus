import time
import os
import arcpy
import autoLin
def main():
    start_time = time.strftime("%m%d_%H%M%S")
    print(f"Time {start_time} - Script started")
    arcpy.CheckOutExtension("3D")
    print(f"Time {time.strftime('%m%d_%H%M%S')} - arcpy imported")
    arcpy.gp.overwriteOutput = True
    terrain = r"D:\Kuba\PhD_data\Thesis\AutoLin\Zdroje\Mentlik\Srni\DMR.gdb\Prasily\Prasily_Terrain"
    resolutions = range(10, 11, 5)
    outDEM_template = r"d:\Kuba\PhD_data\Thesis\AutoLin\DEM\Prasily\LLS\pr_lls_dem_"
    for cell_size in resolutions:
        outDEM = f"{outDEM_template}{cell_size}"
        if not os.path.exists(outDEM):
            tempDEM = os.path.join(autoLin.getDir(outDEM), "tempDEM")
            if not os.path.exists(tempDEM):
                arcpy.TerrainToRaster_3d(
                    terrain, tempDEM, "FLOAT", "LINEAR", f"CELLSIZE {cell_size}", "0"
                )
            try:
                print(f"Time {time.strftime('%m%d_%H%M%S')} - Filling DEM {outDEM}")
                arcpy.gp.Fill_sa(tempDEM, outDEM)
            except Exception as e:
                print(f"DEM {outDEM} failed - {e} - Skipping to next resolution")
                autoLin.deletePath(tempDEM)
                continue
            autoLin.deletePath(tempDEM)
        else:
            print(f"Skipping DEM {outDEM}, already exists")
    arcpy.CheckInExtension("3D")
    print(f"Time {time.strftime('%m%d_%H%M%S')} - Script finished")
if __name__ == "__main__":
    main()