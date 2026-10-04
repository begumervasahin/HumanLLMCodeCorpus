import os
workspace = r"c:\Users\jsilhavy\Documents\GitHub\MHHC\mhhc\sample" + os.path.sep
workspacePCI = "C:" + os.path.sep
resultsDir = os.path.join(workspace, "Results") + os.path.sep
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
for key, folder in workspace_dirs.items():
    workspace_dirs[key] = os.path.join(workspace, folder) + os.path.sep
DEMs = ["sa_sr_dem_30"]
sourceDir = os.path.join(workspace, "DEM") + os.path.sep
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
rotationStep = 9
rotationMax = 45
rotations = range(0, rotationMax, rotationStep)
def getCellSize(DEM):
    codeSApos = DEM.rfind("_")
    return int(DEM[codeSApos+1:])
def getSA(DEM):
    codeSApos = DEM.find("_")
    codeSA = DEM[:codeSApos]
    return "SampleArea" if codeSA == "sa" else codeSA
def getInputMXDPath(SA):
    return os.path.join(workspace_dirs['imageData'], f"{SA}.mxd")
def getSourceDEM(DEM):
    codeSApos = DEM.find("_")
    codeSourceDEMpos = DEM[codeSApos+1:].find("_") + codeSApos + 1
    codeSourceDEM = DEM[codeSApos+1:codeSourceDEMpos]
    sourceDEM_map = {
        "zm": "ZM50",
        "lls": "LLS",
        "d4": "DMR4G",
        "d5": "DMR5G",
        "d": "DMU25",
        "as": "ASTER",
        "sr": "SRTM"
    }
    return sourceDEM_map.get(codeSourceDEM, codeSourceDEM)
def getBufferSizeCluster():
    bufferSizeClusterMin = 100
    bufferSizeClusterMax = 200
    return [bufferSizeClusterMin, bufferSizeClusterMax]
def getRotationAngle(DEM):
    codeSApos = DEM.rfind("_")
    codeRotation = DEM.find("_r")
    return int(DEM[codeRotation+2:codeSApos])
def getHSAzimuth(shpName):
    angleStart = shpName.find("_") + 1
    angleEnd = shpName.find("_", angleStart)
    return shpName[angleStart:angleEnd]
for dem in DEMs:
    print("Cell Size:", getCellSize(dem))
    print("Sample Area:", getSA(dem))
    print("Input MXD Path:", getInputMXDPath(getSA(dem)))
    print("Source DEM:", getSourceDEM(dem))
    print("Rotation Angle:", getRotationAngle(dem))
    print("Buffer Sizes:", getBufferSizeCluster())