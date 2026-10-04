import os
b1 = r"c:\Users\jsilhavy\Documents\GitHub\MHHC\mhhc\sample"
b2 = "C:" + os.path.sep
b3 = os.path.join(b1, "Results")
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
b6 = {key: os.path.join(b1, folder) for key, folder in b6.items()}
b7 = ["sa_sr_dem_30"]
b8 = os.path.join(b1, "DEM")
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
a11 = 9
a12 = 45
b16 = range(0, a12, a11)
def fonk1(DEM):
    return int(DEM.split('_')[-1])
def fonk2(DEM):
    return "SampleArea" if DEM.startswith("sa_") else DEM.split('_')[0]
def fonk3(SA):
    return os.path.join(b6['imageDataWS'], f"{SA}.mxd")
def fonk4(DEM):
    b17 = DEM.split('_')[1]
    b18 = {
        "zm": "ZM50",
        "lls": "LLS",
        "d4": "DMR4G",
        "d5": "DMR5G",
        "d": "DMU25",
        "as": "ASTER",
        "sr": "SRTM"
    }
    return b18.get(b17, b17)
def fonk5():
    return [100, 200]
def fonk6(DEM):
    b19 = DEM.split('_r')[-1]
    return int(b19.split('_')[0])
def fonk7(shp_name):
    return shp_name.split('_')[1]
for dem in b7:
    print("Cell Size:", fonk1(dem))
    print("Sample Area:", fonk2(dem))
    print("Input MXD Path:", fonk3(fonk2(dem)))
    print("Source DEM:", fonk4(dem))
    print("Rotation Angle:", fonk6(dem))
    print("Buffer Sizes:", fonk5())