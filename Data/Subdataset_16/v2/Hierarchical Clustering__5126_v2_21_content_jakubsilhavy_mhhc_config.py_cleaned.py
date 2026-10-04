import os
b1 = r"c:\Users\jsilhavy\Documents\GitHub\MHHC\mhhc\sample" + os.path.sep
b2 = "C:" + os.path.sep
b3 = os.path.join(b1, "Results") + os.path.sep
b4 = True
b5 = False
b6 = {
    "hlWS": "HLs",
    "combiWS": "process",
    "runEAS": "runEAS",
    "shpWS": "shp",
    "shpLinesWS": "shpLines",
    "negativeWS": "negative",
    "positiveWS": "positive",
    "unsureWS": "unsure",
    "temp": "temp",
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
    "imageData": "ImageData"
}
for key, folder in b6.items():
    b6[key] = os.path.join(b1, folder) + os.path.sep
b7 = ["sa_sr_dem_30"]
b8 = os.path.join(b1, "DEM") + os.path.sep
b9 = True
a1 = 400
a2 = 15
a3 = 360
b10 = range(0, a3, a2)
a4 = 30
a5 = 0
a6 = 0
a7 = 1
a8 = 10
a9 = 10
a10 = 10
b11 = "split"
b12 = "relevantMerged.shp"
b13 = "relevantMerged_lite.shp"
b14 = {
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
b15 = {
    "yMax": 4,
    "radMax": 5,
    "gisExePath": r"ProgramKIV\GIS_linie_4\gis.exe",
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
a11 = 9
a12 = 45
b16 = range(0, a12, a11)
def fonk1(DEM):
    b17 = DEM.rfind("_")
    return int(DEM[b17+1:])
def fonk2(DEM):
    b17 = DEM.find("_")
    b18 = DEM[:b17]
    return "SampleArea" if b18 = = "sa" else b18
def fonk3(SA):
    return os.path.join(b6['imageData'], f"{SA}.mxd")
def fonk4(DEM):
    b17 = DEM.find("_")
    b19 = DEM[b17+1:].find("_") + b17 + 1
    b20 = DEM[b17+1:b19]
    b21 = {
        "zm": "ZM50",
        "lls": "LLS",
        "d4": "DMR4G",
        "d5": "DMR5G",
        "d": "DMU25",
        "as": "ASTER",
        "sr": "SRTM"
    }
    return b21.get(b20, b20)
def fonk5():
    a13 = 100
    a14 = 200
    return [a13, a14]
def fonk6(DEM):
    b17 = DEM.rfind("_")
    b22 = DEM.find("_r")
    return int(DEM[b22+2:b17])
def fonk7(shpName):
    b23 = shpName.find("_") + 1
    b24 = shpName.find("_", b23)
    return shpName[b23:b24]
for dem in b7:
    print("Cell Size:", fonk1(dem))
    print("Sample Area:", fonk2(dem))
    print("Input MXD Path:", fonk3(fonk2(dem)))
    print("Source DEM:", fonk4(dem))
    print("Rotation Angle:", fonk6(dem))
    print("Buffer Sizes:", fonk5())