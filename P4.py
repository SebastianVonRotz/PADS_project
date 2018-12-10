"""
Title: 
From: Sebastian von Rotz
Desription:
"""
import P3
import P2
import numpy as np
#---------------------------------------------------------------------------------------------------------#
# def InputCheck ()


#---------------------------------------------------------------------------------------------------------#
def Create2dDict (matrix):
    mainDict = {}
    for i in range(np.shape(matrix)[0]):
        nestedDict = {}
        for j in range(np.shape(matrix)[0]):
            if i != j : #and j+1 not in mainDict and i+1 not in nestedDict
                nestedDict[j+1] = matrix[i,j]
            continue
        if bool(nestedDict) != False:
            mainDict[i+1] = nestedDict
    return mainDict

#---------------------------------------------------------------------------------------------------------#
def FindMinValue(multiDimDict):
    #The minimum value and keys are initialized with arbitrary numbers
    minValue = 1000
    minKey = 1
    minKey2 = 2
    for key in multiDimDict:
        for key2 in multiDimDict[key]:
            if multiDimDict[key][key2] < minValue:
                minValue = multiDimDict[key][key2]
                minKey = key
                minKey2 = key2
    return multiDimDict, multiDimDict[minKey][minKey2], minKey, minKey2

#---------------------------------------------------------------------------------------------------------#
def RecalculateDict (multiDimDict, minValue, minKey, minKey2):
    for key in multiDimDict:
        if key == minKey:
            newNestedDict = {}
            for key2 in multiDimDict[key]:
                if minKey != key2 and minKey2 != key2:
                    newClusterPairValue = (multiDimDict[minKey][key2] + multiDimDict[minKey2][key2])/2
                    newNestedDict[key2] = newClusterPairValue
                continue
            newKeynestedDict = minKey,minKey2
            multiDimDict[newKeynestedDict] = newNestedDict
            break

    for key in multiDimDict:
        if newKeynestedDict not in multiDimDict[key] and key != minKey and key != minKey2 and key != newKeynestedDict:
            newClusterPairValue = (multiDimDict[minKey][key] + multiDimDict[minKey2][key])/2
            multiDimDict[key][newKeynestedDict] = newClusterPairValue

    del multiDimDict[minKey]
    del multiDimDict[minKey2]
    for key in multiDimDict:
        if minKey in multiDimDict[key]:
            del multiDimDict[key][minKey]
    for key in multiDimDict:
        if minKey2 in multiDimDict[key]: 
            del multiDimDict[key][minKey2]
    return multiDimDict

#---------------------------------------------------------------------------------------------------------#
def ClusterRun (nestedDict):
    listWithFourValues = FindMinValue(nestedDict)
    newNestedDict = RecalculateDict(listWithFourValues[0],listWithFourValues[1],listWithFourValues[2],listWithFourValues[3])
    return newNestedDict

#---------------------------------------------------------------------------------------------------------#
testmatrix = np.array([[0, 17, 21, 31, 23],
                      [17, 0, 30, 34, 21],
                      [21, 30, 0, 28, 39],
                      [31, 34, 28, 0, 43],
                      [23, 21, 39, 43, 0]]) 

def Cluster ():
    distMatrix = P3.ComputeDistMatrix()
    # distMatrix = testmatrix
    nestedDict = Create2dDict(distMatrix)
    for runs in range(np.shape(distMatrix)[0]-1):
        nestedDict = ClusterRun(nestedDict)

    #exchange the numbers with the according labels from P2 (P2.LabelDict())
    
    for key in nestedDict:
        print ("The key is" + " " + key)

Cluster()




# testmatrix = np.array([[0, 17, 21, 31, 23],
#                     [17, 0, 30,	34,	21],
#                     [21, 30, 0,	28,	39],
#                     [31, 34, 28, 0,	43],
#                     [23, 21, 39, 43, 0]])   



