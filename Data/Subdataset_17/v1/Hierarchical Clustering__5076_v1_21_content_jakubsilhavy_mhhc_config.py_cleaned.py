import os
workspace = r"c:\Users\jsilhavy\Documents\GitHub\MHHC\mhhc\sample" + os.path.sep
workspacePCI = "C:" + os.path.sep
resultsDir = workspace + "Results" + os.path.sep
hasPCIdone = True
onlyHiearchy = False
hlWS = os.path.join(workspace, "HLs" + os.path.sep)
combiWS = os.path.join(workspace, "process" + os.path.sep)
runEAS = os.path.join(workspace, "runEAS" + os.path.sep)
shpWS = os.path.join(workspace, "shp" + os.path.sep)
shpLinesWS = os.path.join(workspace, "shpLines" + os.path.sep)
negativeWS = os.path.join(workspace, "negative" + os.path.sep)
positiveWS = os.path.join(workspace, "positive" + os.path.sep)
unsureWS = os.path.join(workspace, "unsure" + os.path.sep)
temp = os.path.join(workspace, "temp" + os.path.sep)
flowWS = os.path.join(workspace, "flow" + os.path.sep)
relevantWS = os.path.join(workspace, "relevant" + os.path.sep)
outAllWS = os.path.join(workspace, "outAll" + os.path.sep)
mergeWS = os.path.join(workspace, "merge" + os.path.sep)
easiWS = os.path.join(workspace, "easi" + os.path.sep)
scriptWS = os.path.join(workspace, "EAS" + os.path.sep)
bundleWS = os.path.join(workspace, "bundle" + os.path.sep)
streamWS = os.path.join(workspace, "stream" + os.path.sep)
shpRotateWS = os.path.join(workspace, "shpRotate" + os.path.sep)
clearWS = os.path.join(workspace, "clear" + os.path.sep)
histWS = os.path.join(workspace, "hist" + os.path.sep)
imageData = os.path.join(workspace, "ImageData" + os.path.sep)
DEMs = ["sa_sr_dem_30"]
sourceDir = os.path.join(workspace, "DEM" + os.path.sep)
isDEMNotRectangle = 1
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
parMeaNon = 2
parMeaRel = 4
parMedNon = 2
parMedRel = 4
relevantT = 3
azimuthTreshold = 20
clusterT = 4
filterCount = 4
memorySaving = 1
optimalStop = 2000
averageMethod = "centroid"
yMax = 4
radMax = 5
gisExePath = r"ProgramKIV\GIS_linie_4\gis.exe"
xKIV = 150
yKIV = 200
clusterTKIV = 1
filterCountKIV = 4
bundleMergedName = "bundleMerged.shp"
bufferSizeRidges = 30
parMeaRidge = 10
parMeaValley = 50
parMedRidge = 2
parMedValley = 15
rotationStep = 9
rotationMax = 45
rotations = range(0, rotationMax, rotationStep)
def getCellSize(DEM):
    codeSApos = DEM.rfind("_")
    return int(DEM[codeSApos+1:])
def getSA(DEM):
    codeSApos = DEM.find("_")
    codeSA = DEM[:codeSApos]
    if codeSA == "sa":
        return "SampleArea"
    else:
        return codeSA
def getInputMXDPath(SA):
    return os.path.join(workspace, imageData, f"{SA}.mxd")
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