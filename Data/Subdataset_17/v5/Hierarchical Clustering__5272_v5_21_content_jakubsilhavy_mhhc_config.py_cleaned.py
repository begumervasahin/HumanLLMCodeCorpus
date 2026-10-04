import os
workspace = r"c:\Users\jsilhavy\Documents\GitHub\MHHC\mhhc\sample"
workspacePCI = "C:" + os.path.sep
resultsDir = os.path.join(workspace, "Results")
hasPCIdone = True
onlyHierarchy = False
workspace_dirs = {
    "hlWS": "HLs",
    "combiWS": "process",
    "runEAS": "runEAS",
    "shpWS": "shp",
    "shpLinesWS": "shpLines",
    "negativeWS": "negative",
    "positiveWS": "positive",
    "unsureWS": "unsure",
    "tempWS": "temp",
    "flowWS": "flow",
    "relevantWS": "relevant",
    "outAllWS": "outAll",
    "mergeWS": "merge",
    "easiWS": "easi",
    "scriptWS": "EAS",
    "bundleWS": "bundle",
    "streamWS": "stream",
    "shpRotateWS": "shpRotate",
    "clearWS": "clear",
    "histWS": "hist",
    "imageDataWS": "ImageData"
}
workspace_dirs = {key: os.path.join(workspace, folder) for key, folder in workspace_dirs.items()}
DEMs = ["sa_sr_dem_30"]
sourceDir = os.path.join(workspace, "DEM")
isDEMNotRectangle = True
clipDEMSize = 400
azimuthStep = 15
azimuthMax = 360
azimuths = range(0, azimuthMax, azimuthStep)
altitude = 30
athr = 0
dthr = 0
fthr = 1
radi = 10
gthr = 10
lthr = 10
splitField = "split"
relevantMergedName = "relevantMerged.shp"
relevantMergedNameLite = "relevantMerged_lite.shp"
clustering_params = {
    "parMeaNon": 2,
    "parMeaRel": 4,
    "parMedNon": 2,
    "parMedRel": 4,
    "relevantT": 3,
    "azimuthThreshold": 20,
    "clusterT": 4,
    "filterCount": 4,
    "memorySaving": True,
    "optimalStop": 2000,
    "averageMethod": "centroid"
}
gis_params = {
    "yMax": 4,
    "radMax": 5,
    "gisExePath": os.path.join("ProgramKIV", "GIS_linie_4", "gis.exe"),
    "xKIV": 150,
    "yKIV": 200,
    "clusterTKIV": 1,
    "filterCountKIV": 4,
    "bundleMergedName": "bundleMerged.shp",
    "bufferSizeRidges": 30,
    "parMeaRidge": 10,
    "parMeaValley": 50,
    "parMedRidge": 2,
    "parMedValley": 15
}
rotationStep = 9
rotationMax = 45
rotations = range(0, rotationMax, rotationStep)
def get_cell_size(DEM):
    return int(DEM.split('_')[-1])
def get_sample_area(DEM):
    return "SampleArea" if DEM.startswith("sa_") else DEM.split('_')[0]
def get_input_mxd_path(SA):
    return os.path.join(workspace_dirs['imageDataWS'], f"{SA}.mxd")
def get_source_dem(DEM):
    code_source_dem = DEM.split('_')[1]
    source_dem_map = {
        "zm": "ZM50",
        "lls": "LLS",
        "d4": "DMR4G",
        "d5": "DMR5G",
        "d": "DMU25",
        "as": "ASTER",
        "sr": "SRTM"
    }
    return source_dem_map.get(code_source_dem, code_source_dem)
def get_buffer_size_cluster():
    return [100, 200]
def get_rotation_angle(DEM):
    rotation_part = DEM.split('_r')[-1]
    return int(rotation_part.split('_')[0])
def get_hs_azimuth(shp_name):
    return shp_name.split('_')[1]
for dem in DEMs:
    print("Cell Size:", get_cell_size(dem))
    print("Sample Area:", get_sample_area(dem))
    print("Input MXD Path:", get_input_mxd_path(get_sample_area(dem)))
    print("Source DEM:", get_source_dem(dem))
    print("Rotation Angle:", get_rotation_angle(dem))
    print("Buffer Sizes:", get_buffer_size_cluster())