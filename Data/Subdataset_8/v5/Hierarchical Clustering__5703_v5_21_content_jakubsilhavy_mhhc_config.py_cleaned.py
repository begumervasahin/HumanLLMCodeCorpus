import os
workspace = r"c:\Users\jsilhavy\Documents\GitHub\MHHC\mhhc\sample" + os.path.sep
workspace_pci = r"C:" + os.path.sep
results_dir = os.path.join(workspace, "Results") + os.path.sep
has_pci_done = True
only_hierarchy = False
subdirectories = {
    "hl_ws": "HLs",
    "combi_ws": "process",
    "run_eas": "runEAS",
    "shp_ws": "shp",
    "shp_lines_ws": "shpLines",
    "negative_ws": "negative",
    "positive_ws": "positive",
    "unsure_ws": "unsure",
    "temp": "temp",
    "flow_ws": "flow",
    "relevant_ws": "relevant",
    "out_all_ws": "outAll",
    "merge_ws": "merge",
    "easi_ws": "easi",
    "script_ws": "EAS",
    "bundle_ws": "bundle",
    "stream_ws": "stream",
    "shp_rotate_ws": "shpRotate",
    "clear_ws": "clear",
    "hist_ws": "hist",
    "image_data": "ImageData"
}
DEMs = ["sa_sr_dem_30"]
source_dir = os.path.join(workspace, "DEM") + os.path.sep
is_dem_not_rectangle = 1
clip_dem_size = 400
azimuth_step = 15
azimuth_max = 360
azimuths = range(0, azimuth_max, azimuth_step)
altitude = 30
athr = 0
dthr = 0
fthr = 1
radi = 10
gthr = 10
lthr = 10
split_field = "split"
relevant_merged_name = "relevantMerged.shp"
relevant_merged_name_lite = "relevantMerged_lite.shp"
par_mea_non = 2
par_mea_rel = 4
par_med_non = 2
par_med_rel = 4
relevant_t = 3
azimuth_threshold = 20
cluster_t = 4
filter_count = 4
memory_saving = 1
optimal_stop = 2000
average_method = "centroid"
y_max = 4
rad_max = 5
gis_exe_path = r"ProgramKIV\GIS_linie_4\gis.exe"
x_kiv = 150
y_kiv = 200
cluster_t_kiv = 1
filter_count_kiv = 4
bundle_merged_name = "bundleMerged.shp"
buffer_size_ridges = 30
par_mea_ridge = 10
par_mea_valley = 50
par_med_ridge = 2
par_med_valley = 15
rotation_step = 9
rotation_max = 45
rotations = range(0, rotation_max, rotation_step)
def get_cell_size(dem):
    code_sa_pos = dem.rfind("_")
    return int(dem[code_sa_pos + 1:])
def get_sa(dem):
    code_sa_pos = dem.find("_")
    code_sa = dem[:code_sa_pos]
    return "SampleArea" if code_sa == "sa" else code_sa
def get_input_mxd_path(sa):
    return os.path.join(workspace, image_data, f"{sa}.mxd")
def get_source_dem(dem):
    code_sa_pos = dem.find("_")
    code_source_dem_pos = dem[code_sa_pos + 1:].find("_") + code_sa_pos + 1
    code_source_dem = dem[code_sa_pos + 1:code_source_dem_pos]
    source_dem = {
        "zm": "ZM50",
        "lls": "LLS",
        "d4": "DMR4G",
        "d5": "DMR5G",
        "d": "DMU25",
        "as": "ASTER",
        "sr": "SRTM"
    }.get(code_source_dem, code_source_dem)
    return source_dem
def get_buffer_size_cluster():
    return [100, 200]
def get_rotation_angle(dem):
    code_sa_pos = dem.rfind("_")
    code_rotation = dem.find("_r")
    return int(dem[code_rotation + 2:code_sa_pos])
def get_hs_azimuth(shp_name):
    angle_start = shp_name.find("_") + 1
    angle_end = shp_name.find("_", angle_start)
    return shp_name[angle_start:angle_end]