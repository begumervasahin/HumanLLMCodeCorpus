import os
b1 = r"c:\Users\jsilhavy\Documents\GitHub\MHHC\mhhc\sample" + os.path.sep
b2 = "C:" + os.path.sep
b3 = b1 + "Results" + os.path.sep
b4 = True
b5 = False
b6 = "HLs" + os.path.sep
b7 = "process" + os.path.sep
b8 = "runEAS" + os.path.sep
b9 = "shp" + os.path.sep
b10 = "shpLines" + os.path.sep
b11 = "negative" + os.path.sep
b12 = "positive" + os.path.sep
b13 = "unsure" + os.path.sep
b14 = "b14" + os.path.sep
b15 = "flow" + os.path.sep
b16 = "relevant" + os.path.sep
b17 = "outAll" + os.path.sep
b18 = "merge" + os.path.sep
b19 = "easi" + os.path.sep
b20 = "EAS" + os.path.sep
b21 = "bundle" + os.path.sep
b22 = "stream" + os.path.sep
b23 = "shpRotate" + os.path.sep
b24 = "clear" + os.path.sep
b25 = "hist" + os.path.sep
b26 = "ImageData" + os.path.sep
b27 = ["sa_sr_dem_30"]
b28 = b1 + "DEM" + os.path.sep
a1 = 1
a2 = 400
a3 = 15
a4 = 360
b29 = range(0, a4, a3)
a5 = 30
a6 = 0
a7 = 0
a8 = 1
a9 = 10
a10 = 10
a11 = 10
b30 = "split"
b31 = "relevantMerged.shp"
b32 = "relevantMerged_lite.shp"
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
b33 = "centroid"
a22 = 4
a23 = 5
b34 = r"ProgramKIV\GIS_linie_4\gis.exe"
a24 = 150
a25 = 200
a26 = 1
a27 = 4
b35 = "bundleMerged.shp"
a28 = 30
a29 = 10
a30 = 50
a31 = 2
a32 = 15
a33 = 9
a34 = 45
b36 = range(0, a34, a33)
def fonk1(dem):
    b37 = dem.rfind("_")
    return int(dem[b37 + 1:])
def fonk2(dem):
    b37 = dem.find("_")
    b38 = dem[0:b37]
    if b38 = = "b39":
        b39 = "SampleArea"
    else:
        b39 = b38
    return b39
def fonk3(b39):
    return b1 + b26 + f"{b39}.mxd"
def fonk4(dem):
    b37 = dem.find("_")
    b40 = dem[b37 + 1:].find("_") + b37 + 1
    b41 = dem[b37 + 1:b40]
    if b41 = = "zm":
        b42 = "ZM50"
    elif b41 = = "lls":
        b42 = "LLS"
    elif b41 = = "d4":
        b42 = "DMR4G"
    elif b41 = = "d5":
        b42 = "DMR5G"
    elif b41 = = "d":
        b42 = "DMU25"
    elif b41 = = "as":
        b42 = "ASTER"
    elif b41 = = "sr":
        b42 = "SRTM"
    else:
        b42 = b41
    return b42
def fonk5():
    a35 = 100
    a36 = 200
    return [a35, a36]
def fonk6(dem):
    b37 = dem.rfind("_")
    b43 = dem.find("_r")
    return int(dem[b43 + 2:b37])
def fonk7(shp_name):
    b44 = shp_name.find("_") + 1
    b45 = shp_name.find("_", b44)
    return shp_name[b44:b45]