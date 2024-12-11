import os
b1 = r"c:\Users\jsilhavy\Documents\GitHub\MHHC\mhhc\sample" + os.path.sep
b2 = r"C:" + os.path.sep
b3 = os.path.join(b1, "Results") + os.path.sep
b4 = True
b5 = False
b6 = {
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
b7 = ["sa_sr_dem_30"]
b8 = os.path.join(b1, "DEM") + os.path.sep
a1 = 1
a2 = 400
a3 = 15
a4 = 360
b9 = range(0, a4, a3)
a5 = 30
a6 = 0
a7 = 0
a8 = 1
a9 = 10
a10 = 10
a11 = 10
b10 = "split"
b11 = "relevantMerged.shp"
b12 = "relevantMerged_lite.shp"
a12 = 2
a13 = 4
a14 = 2
a15 = 4
a16 = 3
a17 = 20
a18 = 4
a19 = 4
a20 = 1
a21 = 2000
b13 = "centroid"
a22 = 4
a23 = 5
b14 = r"ProgramKIV\GIS_linie_4\gis.exe"
a24 = 150
a25 = 200
a26 = 1
a27 = 4
b15 = "bundleMerged.shp"
a28 = 30
a29 = 10
a30 = 50
a31 = 2
a32 = 15
a33 = 9
a34 = 45
b16 = range(0, a34, a33)
def fonk1(dem):
    b17 = dem.rfind("_")
    return int(dem[b17 + 1:])
def fonk2(dem):
    b17 = dem.find("_")
    b18 = dem[:b17]
    return "SampleArea" if b18 = = "sa" else b18
def fonk3(sa):
    return os.path.join(b1, image_data, f"{sa}.mxd")
def fonk4(dem):
    b17 = dem.find("_")
    b19 = dem[b17 + 1:].find("_") + b17 + 1
    b20 = dem[b17 + 1:b19]
    b21 = {
        "zm": "ZM50",
        "lls": "LLS",
        "d4": "DMR4G",
        "d5": "DMR5G",
        "d": "DMU25",
        "as": "ASTER",
        "sr": "SRTM"
    }.get(b20, b20)
    return b21
def fonk5():
    return [100, 200]
def fonk6(dem):
    b17 = dem.rfind("_")
    b22 = dem.find("_r")
    return int(dem[b22 + 2:b17])
def fonk7(shp_name):
    b23 = shp_name.find("_") + 1
    b24 = shp_name.find("_", b23)
    return shp_name[b23:b24]