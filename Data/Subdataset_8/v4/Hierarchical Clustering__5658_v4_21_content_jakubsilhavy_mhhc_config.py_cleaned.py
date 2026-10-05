import os
workspace = r"c:\Users\jsilhavy\Documents\GitHub\MHHC\mhhc\sample" + os.path.sep
workspace_pci = "C:" + os.path.sep
results_dir = workspace + "Results" + os.path.sep
has_pci_done = True
only_hierarchy = False
hl_ws = "HLs" + os.path.sep
combi_ws = "process" + os.path.sep
run_eas = "runEAS" + os.path.sep
shp_ws = "shp" + os.path.sep
shp_lines_ws = "shpLines" + os.path.sep
negative_ws = "negative" + os.path.sep
positive_ws = "positive" + os.path.sep
unsure_ws = "unsure" + os.path.sep
temp = "temp" + os.path.sep
flow_ws = "flow" + os.path.sep
relevant_ws = "relevant" + os.path.sep
out_all_ws = "outAll" + os.path.sep
merge_ws = "merge" + os.path.sep
easi_ws = "easi" + os.path.sep
script_ws = "EAS" + os.path.sep
bundle_ws = "bundle" + os.path.sep
stream_ws = "stream" + os.path.sep
shp_rotate_ws = "shpRotate" + os.path.sep
clear_ws = "clear" + os.path.sep
hist_ws = "hist" + os.path.sep
image_data = "ImageData" + os.path.sep
DEMs = ["sa_sr_dem_30"]
source_dir = workspace + "DEM" + os.path.sep
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
    code_sa = dem[0:code_sa_pos]
    if code_sa == "sa":
        sa = "SampleArea"
    else:
        sa = code_sa
    return sa
def get_input_mxd_path(sa):
    return workspace + image_data + f"{sa}.mxd"
def get_source_dem(dem):
    code_sa_pos = dem.find("_")
    code_source_dem_pos = dem[code_sa_pos + 1:].find("_") + code_sa_pos + 1
    code_source_dem = dem[code_sa_pos + 1:code_source_dem_pos]
    if code_source_dem == "zm":
        source_dem = "ZM50"
    elif code_source_dem == "lls":
        source_dem = "LLS"
    elif code_source_dem == "d4":
        source_dem = "DMR4G"
    elif code_source_dem == "d5":
        source_dem = "DMR5G"
    elif code_source_dem == "d":
        source_dem = "DMU25"
    elif code_source_dem == "as":
        source_dem = "ASTER"
    elif code_source_dem == "sr":
        source_dem = "SRTM"
    else:
        source_dem = code_source_dem
    return source_dem
def get_buffer_size_cluster():
    buffer_size_cluster_min = 100
    buffer_size_cluster_max = 200
    return [buffer_size_cluster_min, buffer_size_cluster_max]
def get_rotation_angle(dem):
    code_sa_pos = dem.rfind("_")
    code_rotation = dem.find("_r")
    return int(dem[code_rotation + 2:code_sa_pos])
def get_hs_azimuth(shp_name):
    angle_start = shp_name.find("_") + 1
    angle_end = shp_name.find("_", angle_start)
    return shp_name[angle_start:angle_end]