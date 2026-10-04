import time
import os
import arcpy
import autoLin
def log_time_message(message):
    current_time = time.strftime("%m%d_%H%M%S")
    print(f"Time {current_time} - {message}")
def create_dem_from_terrain(terrain, temp_dem, cell_size):
    arcpy.TerrainToRaster_3d(
        terrain, temp_dem, "FLOAT", "LINEAR", f"CELLSIZE {cell_size}", "0"
    )
def fill_dem(temp_dem, out_dem):
    arcpy.gp.Fill_sa(temp_dem, out_dem)
def process_dem(terrain, out_dem, cell_size):
    temp_dem = os.path.join(autoLin.getDir(out_dem), "tempDEM")
    if not os.path.exists(temp_dem):
        create_dem_from_terrain(terrain, temp_dem, cell_size)
    try:
        log_time_message(f"Filling DEM {out_dem}")
        fill_dem(temp_dem, out_dem)
    except Exception as e:
        log_time_message(f"DEM {out_dem} failed - {e} - Skipping to next resolution")
        autoLin.deletePath(temp_dem)
        return
    autoLin.deletePath(temp_dem)
def main():
    log_time_message("Script started")
    arcpy.CheckOutExtension("3D")
    log_time_message("arcpy imported")
    arcpy.gp.overwriteOutput = True
    terrain = r"D:\Kuba\PhD_data\Thesis\AutoLin\Zdroje\Mentlik\Srni\DMR.gdb\Prasily\Prasily_Terrain"
    resolutions = range(10, 11, 5)
    out_dem_template = r"d:\Kuba\PhD_data\Thesis\AutoLin\DEM\Prasily\LLS\pr_lls_dem_"
    for cell_size in resolutions:
        out_dem = f"{out_dem_template}{cell_size}"
        if not os.path.exists(out_dem):
            process_dem(terrain, out_dem, cell_size)
        else:
            log_time_message(f"Skipping DEM {out_dem}, already exists")
    arcpy.CheckInExtension("3D")
    log_time_message("Script finished")
if __name__ == "__main__":
    main()