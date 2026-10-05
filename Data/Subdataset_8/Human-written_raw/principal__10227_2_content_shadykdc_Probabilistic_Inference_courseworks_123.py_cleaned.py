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
            if (jP[i][j] != 0):
                mi += (jP[i][j] * log2(jP[i][j]/(row_sum*col_sum[j])))
    return mi
def DependencyMatrix(theData, noVariables, noStates):
    MIMatrix = zeros((noVariables, noVariables))
    for i in range(noVariables):
        for j in range(i+1):
            jP = JPT(theData, i, j, noStates)
            MIMatrix[i][j] = MutualInformation(jP)
            MIMatrix[j][i] = MIMatrix[i][j]
    return MIMatrix
def DependencyList(depMatrix):
    depList=[]
    num_rows = len(depMatrix[:,0])
    for i in range(num_rows):
        for j in range(i):
            depList.append([depMatrix[i][j], i, j])
    depList2 = sorted(depList, reverse=True)
    return array(depList2)
def merge(vec,root1,root2):
    for i in range(len(vec)):
      if (vec[i]==root2):
	vec[i]=root1
def SpanningTreeAlgorithm(depList, noVariables):
    spanningTree = []
    vec_root=numpy.arange(noVariables)
    arc_list=[[item[1],item[2]] for item in depList]
    for i in range(len(arc_list)):
      node0=arc_list[i][0]
      node1=arc_list[i][1]
      if (vec_root[node0]!=vec_root[node1]):
	merge(vec_root,vec_root[node0],vec_root[node1])
	spanningTree.append(arc_list[i])
    return array(spanningTree)
def CPT_2(theData, child, parent1, parent2, noStates):
    cPT = zeros([noStates[child],noStates[parent1],noStates[parent2]], float )
    for i in range(len(theData)):
        cPT[theData[i, child]][theData[i, parent1]][theData[i, parent2]]+=1
    for i in range(noStates[parent1]):
        for j in range(noStates[parent2]):
            alpha=sum(cPT[:,i,j])
            if alpha!=0:
                cPT[:,i,j]/=alpha
    return cPT
def ExampleBayesianNetwork(theData, noStates):
    arcList = [[0],[1],[2,0],[3,2,1],[4,3],[5,3]]
    cpt0 = Prior(theData, 0, noStates)
    cpt1 = Prior(theData, 1, noStates)
    cpt2 = CPT(theData, 2, 0, noStates)
    cpt3 = CPT_2(theData, 3, 2, 1, noStates)
    cpt4 = CPT(theData, 4, 3, noStates)
    cpt5 = CPT(theData, 5, 3, noStates)
    cptList = [cpt0, cpt1, cpt2, cpt3, cpt4, cpt5]
    return arcList, cptList
def HepatitisCBayesianNet(theData, noStates):
    arcList = [[0],[1],[2,0],[3,4],[4,1],[5,4],[6,1],[7,0,1],[8,7]]
    cpt0 = Prior(theData, 0, noStates)
    cpt1 = Prior(theData, 1, noStates)
    cpt2 = CPT(theData, 2, 0, noStates)
    cpt3 = CPT(theData, 3, 4, noStates)
    cpt4 = CPT(theData, 4, 1, noStates)
    cpt5 = CPT(theData, 5, 4, noStates)
    cpt6 = CPT(theData, 6, 1, noStates)
    cpt7 = CPT_2(theData, 7, 0, 1, noStates)
    cpt8 = CPT(theData, 8, 7, noStates)
    cptList = [cpt0, cpt1, cpt2, cpt3, cpt4, cpt5, cpt6, cpt7, cpt8]
    return arcList, cptList
def TestBayesianNet(theData, noStates):
    arcList = [[0],[1,0],[2,0],[3,1]]
    cpt0 = Prior(theData, 0, noStates)
    cpt1 = Prior(theData, 1, noStates)
    cpt2 = CPT(theData, 2, 0, noStates)
    cpt3 = CPT(theData, 3, 1, noStates)
    cptList = [cpt0, cpt1, cpt2, cpt3]
    return arcList, cptList
def MDLSize(arcList, cptList, noDataPoints, noStates):
    mdlSize = 0.0
    bn = 0
    for aList in arcList:
        to_add = noStates[aList[0]]-1
        for i in xrange(1,len(aList)):
            to_add *= noStates[aList[i]]
        bn += to_add
    mdlSize = bn*log2(noDataPoints)/2
    return mdlSize
def JointProbability(dataPoint, arcList, cptList):
    jP = 1.0
    for i in range(len(dataPoint)):
        if len(arcList[i])==1:
            jP*=cptList[i][dataPoint[i]]
        elif len(arcList[i])==2:
            jP*=(cptList[i])[dataPoint[i]][dataPoint[arcList[i][1]]]
        else:
            jP*=(cptList[i])[dataPoint[i]][dataPoint[arcList[i][1]]][dataPoint[arcList[i][2]]]
    return jP
def MDLAccuracy(theData, arcList, cptList):
    mdlAccuracy=0
    for i in range(len(theData)):
        mdlAccuracy+=log2(JointProbability(theData[i],arcList,cptList))
    return mdlAccuracy
def MDLScore(theData, arcList, cptList,noStates):
    MSize=MDLSize(arcList, cptList,len(theData),noStates)
    MAcc=MDLAccuracy(theData, arcList, cptList)
    mdlScore=MSize-MAcc
    return mdlScore
def BestScoreAfterRemoval(theData,arcList,cptList,noStates):
    scores=[]
    for aList in arcList:
        if len(aList)==2:
            save_cpt=numpy.copy(cptList[aList[0]])
            save_item=aList[1]
            cptList[aList[0]]=Prior(theData,aList[0],noStates)
            aList.remove(save_item)
            scores.append(MDLScore(theData, arcList, cptList,noStates))
            cptList[aList[0]]=numpy.copy(save_cpt)
            aList.append(save_item)
        if len(aList)==3:
            for i in range(1,2):
                save_cpt=numpy.copy(cptList[aList[0]])
                save_item=aList[2] if i==1 else aList[1]
                cptList[aList[0]]=CPT(theData,aList[0],aList[i],noStates)
                aList.remove(save_item)
                scores.append(MDLScore(theData, arcList, cptList,noStates))
                cptList[aList[0]]=numpy.copy(save_cpt)
                aList.append(save_item)
    print(min(scores))
    return min(scores)
noVariables, noRoots, noStates, noDataPoints, datain = ReadFile("HepatitisC.txt")
theData = array(datain)
AppendString("results.txt","Coursework Three Results by Kathryn Shea & Pierre Thary")
AppendString("results.txt","")
AppendString("results.txt","The MDLSize of our network for Hepatitis C data set")
AppendString("results.txt","")
[arclist,cptlist]=HepatitisCBayesianNet(theData, noStates)
mdlsize=MDLSize(arclist,cptlist,len(theData),noStates)
mdlaccuracy=MDLAccuracy(theData,arclist,cptlist)
BestScoreAfterRemoval(theData,arclist,cptlist,noStates)