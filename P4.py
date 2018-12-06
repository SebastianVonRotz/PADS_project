import P3
import numpy as np

distMatrix = P3.ComputeDistMatrix()

def Create2dDict (matrix):
    mainDict = {}
    for i in range(np.shape(matrix)[0]):
        nestedDict = {}
        for j in range(np.shape(matrix)[0]):
            if i != j:
                nestedDict[j+1] = matrix[i,j]
            continue
        mainDict[i+1] = nestedDict
    return mainDict

def FindMinValue(Dict):
    for key in Dict:
        
        print (7)





# def FindMinValue (dict):
#     b = np.ma.MaskedArray(dict, dict <= 0)
#     ind = np.unravel_index(np.argmin(b, axis=None), b.shape)
#     return ind, dict[ind]

# indexAndValue = FindMinValue(distMatrix)
# binaryTree = indexAndValue[0]

# def ReducingMatrix (index, value):
#     distMatrix[ind] = 0.0
#     for i in range(np.shape(distMatrix)[0]):
#         for j in range(np.shape(distMatrix)[0]):
#             if distMatrix[i, j] != 0.0

FindMinValue(Create2dDict(distMatrix))   
