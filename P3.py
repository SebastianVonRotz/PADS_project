"""
Title: Pairwise Distance Matrix
From: Sebastian von Rotz
Desription: The estimated p-distance for each aligned pair is calculated and returned in a new matrix.
"""
import numpy as np
from numpy import log

#---------------------------------------------------------------------------------------------------------#
def InputCheck (alignedSequencesDict):
    """
    Raises exceptions if the Input is not correct.
    -alignedSequencesDict: Dictionary with number labels as keys and aligned sequences as values.
    -returns: None
    """
    if type(alignedSequencesDict) != dict:
         raise RuntimeError("Input to P3 is not a alignedSequencesDict")
    
    for key in alignedSequencesDict:
        if type(key) != tuple:
            raise RuntimeError("A key in the alignedSequencesDict is not a tuple")
        
        elif type(key[0]) != int and type(key[1]) != int:
            raise RuntimeError("A key in the alignedSequencesDict does not contain only integers")

        elif type(alignedSequencesDict[key]) != tuple:
             raise RuntimeError("A value in the alignedSequencesDict is not a tuple")
        
        elif type(alignedSequencesDict[key][0]) != str and type(alignedSequencesDict[key][1]) != str:
             raise RuntimeError("A value in the alignedSequencesDict does not contain only strings")
        
        elif len(alignedSequencesDict[key][0]) != len(alignedSequencesDict[key][1]):
            raise RuntimeError("To squences in a tuple value do not have the same length ")
    return None

#---------------------------------------------------------------------------------------------------------#
def EstimatedPdistance (alignment1, alignment2):
    """
    The estimated p distance is calculated and returned as the d value
    -alignment1: The first alignemnt of a value in the dictionary
    -alignment2: The second alignemnt of a value in the dictionary
    -returns: dValue
    """

    mismatchCount=0
    alignmentLength=0

    # The alignment length will be incremented if the the bases at the comparison site are a match or 
    # different and the mismatchCount is incremented if the bases are different.
    for char in range(len(alignment1)):
        if alignment1[char] == "_" or alignment2[char] == "_":
            continue
        elif alignment1[char] == alignment2[char]:
            alignmentLength +=1
        else:
            mismatchCount += 1
            alignmentLength +=1
    
    #If the p Values is > 3/4 the sequences have diverged too match and the the dValue is set to 30
    if mismatchCount/alignmentLength >= 3/4:
        dValue = 30
    else:
        dValue = -3/4*log(1 - (mismatchCount/alignmentLength)*4/3)
    return dValue

#---------------------------------------------------------------------------------------------------------#
def ComputeDistMatrix(alignedSequencesDict):
    """
    Computes the distances between the alignments in the dictionary
    -alignedSequenceDict: Contains the number labels as keys and the alignments as values
    -returns: distance Matrix containing the calculated d values
    """

    InputCheck(alignedSequencesDict)

    for key in alignedSequencesDict:
        maxKeyValue = 0
        if key[1] > maxKeyValue:
            maxKeyValue = key[1]
    # A new matrix is created with the length of the max value in the keys (e.g. (1,4), (3,7) -> 7)
    distMatrix = np.zeros ((maxKeyValue, maxKeyValue))

    # The new matrix is filled with the estimated p distance values according to the sequences in the
    # dictionary with the sequences.
    for key in alignedSequencesDict:
        distMatrix[key[0]-1, key[1]-1]= round(EstimatedPdistance(alignedSequencesDict[key][0],
                                                                 alignedSequencesDict[key][1]), 5)
        distMatrix[key[1]-1, key[0]-1]= round(EstimatedPdistance(alignedSequencesDict[key][0], 
                                                                 alignedSequencesDict[key][1]), 5)

    return distMatrix



