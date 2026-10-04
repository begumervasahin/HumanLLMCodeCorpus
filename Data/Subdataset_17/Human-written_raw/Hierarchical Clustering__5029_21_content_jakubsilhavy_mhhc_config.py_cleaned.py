import os
workspace = r"c:\Users\jsilhavy\Documents\GitHub\MHHC\mhhc\sample" + os.path.sep
workspacePCI = "C:" + os.path.sep
resultsDir = workspace + "Results" + os.path.sep
hasPCIdone = True
onlyHiearchy = False
hlWS = "HLs" + os.path.sep
combiWS = "process" + os.path.sep
runEAS = "runEAS" + os.path.sep
shpWS = "shp" + os.path.sep
shpLinesWS = "shpLines" + os.path.sep
negativeWS = "negative" + os.path.sep
positiveWS = "positive" + os.path.sep
unsureWS = "unsure" + os.path.sep
temp = "temp" + os.path.sep
flowWS = "flow" + os.path.sep
relevantWS = "relevant" + os.path.sep
outAllWS =  "outAll" + os.path.sep
mergeWS = "merge" + os.path.sep
easiWS = "easi" + os.path.sep
scriptWS = "EAS" + os.path.sep
bundleWS = "bundle" + os.path.sep
streamWS = "stream" + os.path.sep
shpRotateWS = "shpRotate" + os.path.sep
clearWS =  "clear" + os.path.sep
histWS = "hist" + os.path.sep
imageData = "ImageData" + os.path.sep
DEMs = ["sa_sr_dem_30"]
sourceDir = workspace + "DEM" + os.path.sep
isDEMNotRectangle = 1
clipDEMSize = 400
azimuthStep = 15
azimuthMax = 360
azimuths = range(0,azimuthMax,azimuthStep)
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
  codeSA =DEM[0:codeSApos]
  if codeSA == "sa":
    SA = "SampleArea"
  else:
    SA = codeSA
  return SA
def getInputMXDPath(SA):
  return workspace + imageData + "%s.mxd" % SA
def getSourceDEM(DEM):
  codeSApos = DEM.find("_")
  codeSourceDEMpos = DEM[codeSApos+1:].find("_") + codeSApos+1
  codeSourceDEM = DEM[codeSApos+1:codeSourceDEMpos]
  if codeSourceDEM == "zm":
    sourceDEM = "ZM50"
  elif codeSourceDEM == "lls":
    sourceDEM = "LLS"
  elif codeSourceDEM == "d4":
    sourceDEM = "DMR4G"
  elif codeSourceDEM == "d5":
    sourceDEM = "DMR5G"
  elif codeSourceDEM == "d":
    sourceDEM = "DMU25"
  elif codeSourceDEM == "as":
    sourceDEM = "ASTER"
  elif codeSourceDEM == "sr":
    sourceDEM = "SRTM"
  else:
    sourceDEM = codeSourceDEM
  return sourceDEM
def getBufferSizeCluster():
  bufferSizeClusterMin = 100
  bufferSizeClusterMax = 200
  return [bufferSizeClusterMin, bufferSizeClusterMax]
def getRotationAngle(DEM):
  codeSApos = DEM.rfind("_")
  codeRotation = DEM.find("_r")
  return int(DEM[codeRotation+2:codeSApos])
def getHSAzimuth(shpName):
  angleStart = shpName.find("_")+1
  angleEnd = shpName.find("_", angleStart)
  return shpName[angleStart:angleEnd]