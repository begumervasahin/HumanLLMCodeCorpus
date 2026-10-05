from IDAPICourseworkLibrary import *
from numpy import *
def Prior(theData, root, noStates):
    prior = zeros((noStates[root]), float )
    data_amount=len(theData[:,0])
    for i in range(data_amount):
        prior[theData[i,root]]+=1
    prior/=data_amount
    return prior
def CPT(theData, varC, varP, noStates):
    data_amount=len(theData[:,0])
    cPT = zeros((noStates[varC], noStates[varP]), float )
    for row in range(data_amount):
        cPT[theData[row,varC]][theData[row,varP]]+=1
    for i in range(noStates[varP]):
        alpha=(numpy.sum(theData[:,varP]==i))
        if alpha!=0:
            cPT[:,i]/=(numpy.sum(theData[:,varP]==i))
    return cPT
def JPT(theData, varRow, varCol, noStates):
    jPT = zeros((noStates[varRow], noStates[varCol]), float )
    data_amount=len(theData[:,0])
    for row in range(data_amount):
        jPT[theData[row,varRow]][theData[row,varCol]]+=1
    jPT/=data_amount
    return jPT
def JPT2CPT(aJPT):
    for i in range(len(aJPT[0,:])):
        alpha=(numpy.sum(aJPT[:,i]))
        if alpha!=0:
            aJPT[:,i]*=1/alpha
    return aJPT
def Query(theQuery, naiveBayes):
    rootPdf = zeros((naiveBayes[0].shape[0]), float)
    for i in range(len(rootPdf)):
        rootPdf[i]=naiveBayes[0][i]
        for j in range(0,len(theQuery)):
            rootPdf[i]*=naiveBayes[j+1][theQuery[j],i]
    if (numpy.sum(rootPdf)!=0):
        rootPdf*=1/(numpy.sum(rootPdf))
    else:
        rootPdf=ones((naiveBayes[0].shape[0]), float)/naiveBayes[0].shape[0]
    return rootPdf
def MutualInformation(jP):
    mi=0.0
    num_cols = len(jP[0,:])
    num_rows = len(jP[:,0])
    col_sum = zeros(num_cols, float)
    for j in range(num_cols):
        col_sum[j] = sum(jP[:,j])
    for i in range(num_rows):
        row_sum = sum(jP[i,:])
        for j in range(num_cols):
            if (jP[i][j] != 0 and col_sum[j] != 0 and row_sum != 0):
                mi+= jP[i][j]*math.log(jP[i][j]/(row_sum*col_sum[j]),2)
    return mi
theData = array([[1,1,1,1],[1,2,1,1],[2,1,2,2],[2,2,2,2],[2,2,1,1]])
theQuery = array([0,1,1])
prior = Prior(theData, 0, [3,2,2,2])
print("Prior:", prior)
cpt = CPT(theData, 1, 0, [3,2,2,2])
print("CPT:", cpt)
jpt = JPT(theData, 0, 1, [3,2,2,2])
print("JPT:", jpt)
cpt_from_jpt = JPT2CPT(jpt)
print("CPT from JPT:", cpt_from_jpt)
naiveBayes = [prior, cpt_from_jpt]
for i in range(len(theQuery)):
    print("Query result:", Query(theQuery, naiveBayes))
mutual_info = MutualInformation(jpt)
print("Mutual Information:", mutual_info)