import numpy, csv, math
from ROOT import *
from numpy import linalg as LA
from project_data import project_data
b1 = "../Higgs13TeV_test_118_130_ggh.csv"
b2 = numpy.loadtxt("../Higgs13TeV_train_118_130_ggh.csv", delimiter=",")
b3 = b2[:,0:21].astype(float)
b4 = b2[:,21]
b5 = len(b4)
b6 = len(b3[0])
b7 = math.factorial(b6)/(math.factorial(b6-2)*2)
print "You have %i b6 resulting to %i covariance matrices..." % (b6,b7)
a1 = 0
a2 = 0
for i in range(b5):
  if(b4[i] == 1):
    a1 += 1
  else:
    a2 += 1
b8 = a1
if(a1 > a2):
  b8 = a2
b9 = [[0 for i in range(b6)] for j in range(b8)]
b10 = [[0 for i in range(b6)] for j in range(b8)]
a1 = 0
a2 = 0
for i in range(b5):
  if(b4[i] == 1 and a1 < b8):
    for j in range(b6):
      b9[a1][j] = b3[a1][j]
    a1 += 1
  if(b4[i] == 0 and a2 < b8):
    for j in range(b6):
      b10[a2][j] = b3[a2][j]
    a2 += 1
b11 = ["l1 p_{T}","l1
	     "l2 p_{T}","l2
	     "l3 p_{T}","l3
	     "l4 p_{T}","l4
	     "j1 p_{T}","j1
	     "j2 p_{T}","j2
	     "Njets"]
b12 = [[0 for i in range(b6)] for j in range(b6)]
b13 = TH2D("b13","",21,0,21,21,0,21)
b14 = numpy.sum(b9, axis=0)
b15 = numpy.sum(b10, axis=0)
for st_d in range(b6):
  print "Analysing through dimension: %i ..." % (st_d+1)
  for nd_d in range(b6):
    a3 = 0
    b16 = b14[st_d]/float(b8-1)
    for ip in range(b8):
      b17 = b15[nd_d]/float(b8-1)
      a3 += (b9[ip][st_d]-b16)*(b10[ip][nd_d]-b17)
    b12[st_d][nd_d] = a3/float(b8-1)
    b13.SetBinContent(nd_d+1,b6-st_d,b12[st_d][nd_d])
  b13.GetXaxis().SetBinLabel(st_d+1,b11[st_d])
  b13.GetYaxis().SetBinLabel(b6-st_d,b11[st_d])
b18 = open('full_covariance_matrix.txt','w')
for i in range(b6):
  for j in range(b6):
    b19 = "%f" % b12[i][j]
    b18.write( b19 )
    if(j < b6-1):
      b18.write( "," )
  b18.write( "\n" )
b18.close()
gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetPadLeftMargin(0.14)
gStyle.SetTitleOffset(1.4,"y")
gStyle.SetPaintTextFormat("0.2e")
b20 = TCanvas("b20","",10,10,2300,1000)
b13.Draw("text")
b13.SetTitle("Full Covariance Matrix")
gPad.Update()
b20.Print("plots/Full_covariance_matrix.png")
feigenvalues, b21 = LA.eig(b12)
b22 = TH2D("b22","",21,0,21,22,0,22)
for i in range(len(feigenvalues)):
  for j in range(len(b21[i])):
    b22.SetBinContent(j+1,len(feigenvalues)-i,b21[i][j])
  b22.SetBinContent(i+1,len(feigenvalues),feigenvalues[i])
  b22.GetXaxis().SetBinLabel(i+1,b11[i])
  b22.GetYaxis().SetBinLabel(len(feigenvalues)-i,b11[i])
b22.GetYaxis().SetBinLabel(len(feigenvalues),"eigs")
b22.Draw("text")
b22.SetTitle("Full Eigenvectors")
b20.Print("plots/Full_eigenvectors.png")
b20 = TCanvas("b20","",10,10,1000,1000)
for st_d in range(b6):
  print "\nPlotting through dimension: %i ..." % (st_d+1)
  for nd_d in range(b6):
    b23 = TGraph()
    a4 = 0
    b16 = b14[st_d]/float(b8-1)
    for ip in range(b8):
      b17 = b15[nd_d]/float(b8-1)
      b23.SetPoint(a4,b9[ip][st_d]-b16,b10[ip][nd_d]-b17)
      a4 += 1
    b23.SetMarkerColor(kBlue)
    b23.SetMarkerStyle(2)
    b24 = TMultiGraph()
    b24.Add(b23)
    b24.Draw("ap")
    b24.GetXaxis().SetTitle(b11[st_d])
    b24.GetYaxis().SetTitle(b11[nd_d])
    b25 = TLegend(0.75,0.7,0.95,0.92)
    b25.SetHeader("Original Space")
    b26 = b21[st_d][st_d]/b21[nd_d][st_d]
    b27 = b21[st_d][nd_d]/b21[nd_d][nd_d]
    a5 = 0
    a6 = 0
    if(feigenvalues[st_d] > feigenvalues[nd_d]):
      a5 = b26
      a6 = b27
    else:
      a5 = b27
      a6 = b26
    b28 = numpy.max(b9,axis=1)[nd_d]
    b29 = TF1("b29","[0]*x")
    b29.SetParameter(0,a5)
    b30 = math.fabs(b29.GetX(b28,-1.e3,1.e3))
    b29.SetRange(-b30,b30)
    b29.SetLineColor(kOrange+2)
    b29.SetLineWidth(8)
    b31 = TF1("b31","[0]*x")
    b31.SetParameter(0,a6)
    b30 = math.fabs(b31.GetX(b28,-1.e3,1.e3))
    b29.Draw("l,same")
    b31.Draw("l,same")
    b25.AddEntry(b29,"1^{st} PCA","l")
    b25.AddEntry(b31,"2^{nd} PCA","l")
    b25.Draw()
    gPad.Update()
    b32 = "plots/Covariance_d%i_d%i.png" % (st_d,nd_d)
    b20.Print(b32)
b20.Close()
b20 = TCanvas("b20","",10,10,1000,1000)
print "\nTransposing original dataset..."
b33 = [[0 for i in range(b5)] for j in range(b6)]
for i in range(b6):
  for j in range(b5):
    b33[i][j] = b3[j][i]
print "Transposing signal eigenvectors..."
b34 = [[0 for i in range(b6)] for j in range(b6)]
for i in range(b6):
  for j in range(b6):
    b34[i][j] = b21[j][i]
print "Sorting signal eigenvectors..."
b35 = numpy.argsort(feigenvalues)
b36 = list(reversed(b35))
b37 = []
for i in range(b6):
  b38 = b36[i]
  b37.append( b34[b38] )
b34 = b37
b39 = open('full_eigenvectors.txt','w')
for i in range(len(b34)):
  for j in range(len(b34[0])):
    b40 = "%.15f" % b34[i][j]
    b39.write( b40 )
    if(j < len(b34[0])-1):
      b39.write( "," )
  b39.write( "\n" )
b39.close()
print "Projecting dataset through signal eigenvectors space..."
b41 = [[0 for j in range(len(b34))] for j in range(b5)]
for irow in range(len(b34)):
  for ientry in range(b5):
    a7 = 0
    for icol in range(len(b34[0])):
      a8 = 0
      if(b4[ientry] == 1):
	a8 = b14[icol]/float(b8-1)
      else:
	a8 = b15[icol]/float(b8-1)
      a7 += b34[irow][icol]*(b33[icol][ientry] - a8)
    b41[ientry][irow] = a7
for st_d in range(len(b41[0])):
  print "\nPlotting through dimension: %i ..." % (st_d+1)
  for nd_d in range(len(b41[0])):
    b42 = TGraph()
    b43 = TGraph()
    a4 = 0
    a9 = 0
    for ip in range(b5):
      if(b4[ip] == 1):
	b42.SetPoint(a4,b41[ip][st_d],b41[ip][nd_d])
	a4 += 1
      else:
	b43.SetPoint(a9,b41[ip][st_d],b41[ip][nd_d])
	a9 += 1
    b42.SetMarkerColor(kBlue)
    b42.SetMarkerStyle(2)
    b43.SetMarkerColor(kRed)
    b43.SetMarkerStyle(2)
    b24 = TMultiGraph()
    b24.Add(b42)
    b24.Add(b43)
    b24.Draw("ap")
    b24.GetXaxis().SetTitle("
    b24.GetYaxis().SetTitle("
    b25 = TLegend(0.15,0.8,0.37,0.92)
    b25.SetHeader("Sig Space")
    b25.AddEntry(b42,"Signal","p")
    b25.AddEntry(b43,"Background","p")
    b25.Draw()
    gPad.Update()
    b32 = "projected_plots/Covariance_d%i_d%i.png" % (st_d,nd_d)
    b20.Print(b32)
b44 = numpy.loadtxt(b1, delimiter=",")
b45 = b2[:,0:21].astype(float)
b46 = len(b45)
b47 = project_data(b45,'full_eigenvectors.txt')
for st_d in range(len(b47[0])):
  print "\nPlotting through dimension: %i ..." % (st_d+1)
  for nd_d in range(len(b47[0])):
    b48 = TGraph()
    b49 = TGraph()
    a4 = 0
    a9 = 0
    for ip in range(b5):
      if(b4[ip] == 1):
	b48.SetPoint(a4,b47[ip][st_d],b47[ip][nd_d])
	a4 += 1
      else:
	b49.SetPoint(a9,b47[ip][st_d],b47[ip][nd_d])
	a9 += 1
    b48.SetMarkerColor(kBlue)
    b48.SetMarkerStyle(2)
    b49.SetMarkerColor(kRed)
    b49.SetMarkerStyle(2)
    b24 = TMultiGraph()
    b24.Add(b48)
    b24.Add(b49)
    b24.Draw("ap")
    b24.GetXaxis().SetTitle("
    b24.GetYaxis().SetTitle("
    b25 = TLegend(0.15,0.8,0.37,0.92)
    b25.SetHeader("Bkg Space")
    b25.AddEntry(b48,"Signal","p")
    b25.AddEntry(b49,"Background","p")
    b25.Draw()
    gPad.Update()
    b32 = "new_test/Covariance_d%i_d%i.png" % (st_d,nd_d)
    b20.Print(b32)