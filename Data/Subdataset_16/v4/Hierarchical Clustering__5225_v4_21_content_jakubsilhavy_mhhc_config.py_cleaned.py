import os
b1 = os.path.join(r"c:\Users\jsilhavy\Documents\GitHub\MHHC\mhhc\sample")
b2 = "C:" + os.path.sep
b3 = os.path.join(b1, "Results")
b4 = True
b5 = False
b6 = os.path.join(b1, "HLs")
b7 = os.path.join(b1, "process")
b8 = os.path.join(b1, "b8")
b9 = os.path.join(b1, "shp")
b10 = os.path.join(b1, "shpLines")
b11 = os.path.join(b1, "negative")
b12 = os.path.join(b1, "positive")
b13 = os.path.join(b1, "unsure")
b14 = os.path.join(b1, "temp")
b15 = os.path.join(b1, "flow")
b16 = os.path.join(b1, "relevant")
b17 = os.path.join(b1, "outAll")
b18 = os.path.join(b1, "merge")
b19 = os.path.join(b1, "easi")
b20 = os.path.join(b1, "EAS")
b21 = os.path.join(b1, "bundle")
b22 = os.path.join(b1, "stream")
b23 = os.path.join(b1, "shpRotate")
b24 = os.path.join(b1, "clear")
b25 = os.path.join(b1, "hist")
b26 = os.path.join(b1, "ImageData")
b27 = ["sa_sr_dem_30"]
b28 = os.path.join(b1, "DEM")
b29 = True
a1 = 400
a2 = 15
a3 = 360
b30 = range(0, a3, a2)
a4 = 30
a5 = 0
a6 = 0
a7 = 1
a8 = 10
a9 = 10
a10 = 10
b31 = "split"
b32 = "relevantMerged.shp"
b33 = "relevantMerged_lite.shp"
a11 = 2
a12 = 4
a13 = 2
a14 = 4
a15 = 3
a16 = 20
a17 = 4
a18 = 4
b34 = True
a19 = 2000
b35 = "centroid"
a20 = 4
a21 = 5
b36 = os.path.join("ProgramKIV", "GIS_linie_4", "gis.exe")
a22 = 150
a23 = 200
a24 = 1
a25 = 4
b37 = "bundleMerged.shp"
a26 = 30
a27 = 10
a28 = 50
a29 = 2
a30 = 15
a31 = 9
a32 = 45
b38 = range(0, a32, a31)
def fonk1(DEM):
    b39 = DEM.rfind("_")
    return int(DEM[b39 + 1:])
def fonk2(DEM):
    b39 = DEM.find("_")
    b40 = DEM[:b39]
    return "SampleArea" if b40 = = "sa" else b40
def fonk3(SA):
    return os.path.join(b26, f"{SA}.mxd")
def fonk4(DEM):
    b39 = DEM.find("_")
    b41 = DEM[b39 + 1:].find("_") + b39 + 1
    b42 = DEM[b39 + 1:b41]
    b43 = {
        "zm": "ZM50",
        "lls": "LLS",
        "d4": "DMR4G",
        "d5": "DMR5G",
        "d": "DMU25",
        "as": "ASTER",
        "sr": "SRTM"
    }
    return b43.get(b42, b42)
def fonk5():
    return [100, 200]
def fonk6(DEM):
    b44 = DEM.find("_r")
    b39 = DEM.rfind("_")
    return int(DEM[b44 + 2:b39])
def fonk7(shpName):
    b45 = shpName.find("_") + 1
    b46 = shpName.find("_", b45)
    return shpName[b45:b46]
for dem in b27:
    print("Cell Size:", fonk1(dem))
    print("Sample Area:", fonk2(dem))
    print("Input MXD Path:", fonk3(fonk2(dem)))
    print("Source DEM:", fonk4(dem))
    print("Rotation Angle:", fonk6(dem))
    print("Buffer Sizes:", fonk5())