"""
Title: Clustering
From: Sebastian von Rotz
Desription: A nested dictionary is created out of the input distance matrix. The clustering (WPGMA)
happens in several instances, where each run finds the minimum distance value in the nested dictionary
and calculates the new key pair and the corresponding new distance values. Also the paired key and its 
corresponding values are deleted and the new nested dictionary is returned. This whole procedure is 
repeated till only one key is left which represents the final cluster of the binary tree.
"""
import numpy as np

#---------------------------------------------------------------------------------------------------------#
def InputCheck (distMatrix, labelList):
    if np.ndim(distMatrix) != 2:
         raise RuntimeError("Input Matrix is not 2 dimensional")
    
    elif np.shape(distMatrix)[0] != np.shape(distMatrix)[1]:
        raise RuntimeError("Matrix is not symmetrical")
    
    if distMatrix.dtype != "float64":
        raise RuntimeError("Matrix values are not floats")

    if type(labelList) != list:
        raise RuntimeError("Input list type is not a list")

    if len(labelList) != np.shape(distMatrix)[0]:
        raise RuntimeError("Number of labels not equal to Matrix size")
    return None

#---------------------------------------------------------------------------------------------------------#
def CreateNestedDict (distMatrix, labelList):
    """
    Creates a nested dictionary out of a matrix
    -distMatrix Is a two dimensinal symmetrical matrix with floats as values
    -labelList: Contains the labels accordingly to the number key in the distMatrix
    -returns: A nested dictionary with the distance values
    """

    distDict = {}
    for i in range(np.shape(distMatrix)[0]):
        nestedDict = {}
        for j in range(np.shape(distMatrix)[0]):
            if i != j :
                nestedDict[labelList[j]] = distMatrix[i,j]
            continue

        # In order not to fill the main dict with an empty nested dict the following check is applied
        if bool(nestedDict) != False:
            distDict[labelList[i]] = nestedDict
    return distDict

#---------------------------------------------------------------------------------------------------------#
def FindMinValue(distDict):
    """
    Find the smalles value in a dictionary
    -distDict: Is a two dimensinal symmetrical matrix with floats as values
    -returns: The same dictionary, the minimum value, corresponding Keys
    """

    #The minimum value and keys are initialized with arbitrary numbers
    minValue = 1000
    minKey = 1
    minKey2 = 2
    # The minimum distance value and the corresponding keys are returned in addition to the input dictionary
    for key in distDict:
        for key2 in distDict[key]:
            if distDict[key][key2] < minValue:
                minValue = distDict[key][key2]
                minKey = key
                minKey2 = key2

    return distDict, distDict[minKey][minKey2], minKey, minKey2

#---------------------------------------------------------------------------------------------------------#
def RecalculateDict (distDict, minValue, minKey, minKey2):
    """
    Creates a cluster pair and deletes the clustered distance values
    -distDict: Is a two dimensinal symmetrical matrix with floats as values
    -minValue: Smallest value in the dictionary
    -minKey: First corresponding key to the smalles value in the dictionary
    -minKey2: Second corresponding key to the smalles value in the dictionary
    -returns: a recalculated distance dictionary with a new clustere pair
    """

    for key in distDict:
        # In order to calculate the new distance values with the clustered keys, the dictionary is searched 
        # for the Key with the minimum distance value (calculated in FindMinValue()).
        if key == minKey:
            newNestedDict = {}
            # The amount of new distance values in the new clustered key equals the amount of nested keys 
            # in the key with the minimum distance value
            for key2 in distDict[key]:
                # New distance values are recalculated only for the nested key position which are not the 
                # keys which contain the minimum distance value.
                if minKey != key2 and minKey2 != key2:
                    newClusterPairValue = (distDict[minKey][key2] + distDict[minKey2][key2])/2
                    newNestedDict[key2] = newClusterPairValue
                continue
            # The newly calculated nested dictionary is added to the main dictionary (distDict).  
            newKeynestedDict = minKey,minKey2
            distDict[newKeynestedDict] = newNestedDict
            break

    # The new distance values in the clustered nested dictionary also have to be added to the 
    # other postions (e.g. Dictionary{[(1,2)][3]:value} -> Dictionary{[3][(1,2)]:value}.
    for key in distDict:
        if (newKeynestedDict not in distDict[key] and key != minKey and 
        key != minKey2 and key != newKeynestedDict):
            newClusterPairValue = (distDict[minKey][key] + distDict[minKey2][key])/2
            distDict[key][newKeynestedDict] = newClusterPairValue

    # All of the previuosly calculated minimum distance values and the corresponding keys (minKey, minKey2)
    # are deleted after recalculating the distance values for the new clustered pair key.
    del distDict[minKey]
    del distDict[minKey2]
    for key in distDict:
        if minKey in distDict[key]:
            del distDict[key][minKey]
    for key in distDict:
        if minKey2 in distDict[key]: 
            del distDict[key][minKey2]

    return distDict

#---------------------------------------------------------------------------------------------------------#
def ClusterRun (distDict):
    """
    Runs on instance of finding the minimum value in the dict and then clutering it one times.
    -distDict: Is a two dimensinal symmetrical matrix with floats as values
    -returns: a recalculated/clustered dictionary
    """

    # One instance of this function finds the minimum distance value in a matrix and recalculates it 
    # with the new clustered key pair and the new distance values.
    listWithFourValues = FindMinValue(distDict)
    distDict = RecalculateDict(listWithFourValues[0],listWithFourValues[1],
                                    listWithFourValues[2],listWithFourValues[3])
    return distDict

#---------------------------------------------------------------------------------------------------------#
def Cluster (distMatrix, labelList):
    """
    Clusters the distance Matrix till only one key is left, which reperesents the binary tree
    -distDict: Is a two dimensinal symmetrical matrix with floats as values
    -labelList: contains the labels accordingly to the number key in the distMatrix
    -returns: a recalculated/clustered dictionary
    """
    InputCheck(distMatrix, labelList)

    # A cluster run is repeated till there is only one key in the dictionary, containing the binary tree.
    nestedDict = CreateNestedDict(distMatrix, labelList)
    for runs in range(np.shape(distMatrix)[0]-1):
        nestedDict = ClusterRun(nestedDict)

    binaryTreeString = str(nestedDict.keys()).replace("dict_keys([", "").replace("])","")

    return binaryTreeString




 



