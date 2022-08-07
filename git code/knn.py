from numpy import *
import operator

def createDataSet():
    characters=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return characters,labels

def file2matrix(filename):
    fr=open(filename)
    arrayOLines=fr.readlines()
    numberOfLines=len(arrayOLines)       
    returnMat=zeros((numberOfLines,3))   
    classLabelVector=[]
    index=0
    for line in arrayOLines:            
        line=line.strip()
        listFromLine=line.split('\t')
        returnMat[index, : ]=listFromLine[0:3]
        classLabelVector.append(listFromLine[-1])
        index+=1
    return returnMat,classLabelVector    

def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataSet=dataSet-tile(minVals,(m,1))
    normDataSet=normDataSet/tile(ranges,(m,1))
    return normDataSet, ranges, minVals
    
def classify(sample,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]     
    diffMat=tile(sample,(dataSetSize,1))-dataSet         
    sqDiffMat=diffMat**2      
    sqDistances=sqDiffMat.sum(axis=1)   
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()   
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


def datingClassTest():
    hoRatio=0.20       
    datingDataMat,datingLabels=file2matrix('datingTestSet1.txt')
    normMat, ranges, minVals=autoNorm(datingDataMat)
    m =normMat.shape[0]
    numTestVecs=int(m*hoRatio)
    errorCount=0.0
    k=4
    for i in range(numTestVecs):
        classifierResult=classify(normMat[i, : ],normMat[numTestVecs:m, : ], datingLabels[numTestVecs:m],k)
        print("The classifier came back with: %s, the real answer is: %s" % (classifierResult, datingLabels[i]))
        if(classifierResult != datingLabels [i] ) :
            errorCount += 1.0
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))

def main():
    sample=[0,0]
    k=3
    group,labels=createDataSet()
    label=classify(sample,group,labels,k)
    print("Classified Label:"+label)

if __name__=='__main__':
    main()
    #datingClassTest()