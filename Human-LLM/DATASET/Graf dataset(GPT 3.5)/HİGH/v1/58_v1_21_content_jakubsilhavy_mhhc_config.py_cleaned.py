import os
b1 = r"c:\Users\jsilhavy\Documents\GitHub\MHHC\mhhc\sample" + os.path.sep
b2 = "C:" + os.path.sep
b3 = os.path.join(b1, "Results") + os.path.sep
b4 = True
b5 = False
b6 = os.path.join(b1, "HLs") + os.path.sep
b7 = os.path.join(b1, "process") + os.path.sep
b8 = os.path.join(b1, "b8") + os.path.sep
b9 = os.path.join(b1, "shp") + os.path.sep
b10 = os.path.join(b1, "shpLines") + os.path.sep
b11 = os.path.join(b1, "negative") + os.path.sep
b12 = os.path.join(b1, "positive") + os.path.sep
b13 = os.path.join(b1, "unsure") + os.path.sep
b14 = os.path.join(b1, "b14") + os.path.sep
b15 = os.path.join(b1, "flow") + os.path.sep
b16 = os.path.join(b1, "relevant") + os.path.sep
b17 = os.path.join(b1, "outAll") + os.path.sep
b18 = os.path.join(b1, "merge") + os.path.sep
b19 = os.path.join(b1, "easi") + os.path.sep
b20 = os.path.join(b1, "EAS") + os.path.sep
b21 = os.path.join(b1, "bundle") + os.path.sep
b22 = os.path.join(b1, "stream") + os.path.sep
b23 = os.path.join(b1, "shpRotate") + os.path.sep
b24 = os.path.join(b1, "clear") + os.path.sep
b25 = os.path.join(b1, "hist") + os.path.sep
b26 = os.path.join(b1, "ImageData") + os.path.sep
b27 = ["sa_sr_dem_30"]
b28 = os.path.join(b1, "DEM") + os.path.sep
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
def fonk1(DEM):
    b37 = DEM.rfind("_")
    return int(DEM[b37+1:])
def fonk2(DEM):
    b37 = DEM.find("_")
    b38 = DEM[0:b37]
    if b38 = = "sa":
        b39 = "SampleArea"
    else:
        b39 = b38
    return b39
def fonk3(b39):
    return os.path.join(b1, b26, "%s.mxd" % b39)
def fonk4(DEM):
    b37 = DEM.find("_")
    b40 = DEM[b37+1:].find("_") + b37+1
    b41 = DEM[b37+1:b40]
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
def fonk6(DEM):
    b37 = DEM.rfind("_")
    b43 = DEM.find("_r")
    return int(DEM[b43+2:b37])
def fonk7(shpName):
    b44 = shpName.find("_")+1
    b45 = shpName.find("_", b44)
    return shpName[b44:b45]