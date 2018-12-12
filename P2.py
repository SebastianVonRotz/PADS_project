"""
Title: Alignmen of Sequences
From: Sebastian von Rotz
Desription: The sequences from P1 are paired, so that each sequences is paired against each other once.
For each pair a Score Matrix with the corresponding traceback Matrix is created. The traceback Matrix is 
then used for the traceback which results in the alignment sequences of each pair.
"""
import numpy as np
import re

#---------------------------------------------------------------------------------------------------------#
def InputCheck (sequenceList):
    """
    Raises exceptions if the Input is not correct.
    -labelSequenceList: list labels and sequences in tuples.
    -returns: None
    """
    if type(sequenceList) != list:
        raise RuntimeError("Data type is not a list")

    for part in range(len(sequenceList)):
        if type(sequenceList[part]) != tuple:
            raise RuntimeError("Part of the list is not a tuple")

        elif type(sequenceList[part][0]) != str:
            raise RuntimeError("Content of your tuple is not a string")
      
        elif type(sequenceList[part][1]) != str:
            raise RuntimeError("Content of your tuple is not a string")

        elif (bool(re.search("^[ACTG]+$", sequenceList[part][1]))) != True:
            raise RuntimeError("Second part a tuple does contain other characters than ATCG") 
    return None

#---------------------------------------------------------------------------------------------------------#
def TracebackMatrix(sequence1, sequence2):
    """
    Creates a score matrix and a traceback matrix.
    -sequence1: first sequence of a pair
    -sequence2: second sequence of a pair
    -returns: matrix for traceback
    """
    array_zero = np.zeros ((len(sequence1)+1, len(sequence2)+1))
    array_traceback= np.zeros ((len(sequence1)+1, len(sequence2)+1))
    
    indel = -6
    match = 5
    mismatch = -2

    # Scoring array starts from 0, therefore -1 for correct character position
    def getScore(i,j):
        """
        Returns the score of a match or mismatch.
        -i: base on a site of sequence1
        -j: base on a site of sequence2
        -returns: match or mismatch score
        """

        if sequence1[i-1] == sequence2[j-1]:
            return match
        else:
            return mismatch

    # The whole first row/column of the previously generated array can be incremented with indel scores
    for i in range(len(sequence1)+1):
        array_zero[i,0]=i*indel
    array_zero
    for j in range(len(sequence2)+1):
        array_zero[0,j]=j*indel
    
    # Filling of the score Matrix and tracking of the max scores in a second matrix for the traceback
    for i in range(1, len(sequence1)+1):
        for j in range(1, len(sequence2)+1):
            diagonal_score = array_zero[i-1, j-1] + getScore(i, j)
            upper_score = array_zero[i-1, j]+ indel
            left_score = array_zero[i, j-1] + indel

            maxScore = max(diagonal_score, upper_score, left_score)
            array_zero[i,j] = maxScore

            if maxScore == diagonal_score:
                array_traceback[i, j] = 1
            elif maxScore == upper_score:
                array_traceback[i, j] = 2     
            else:
                array_traceback[i, j] = 3
    return array_traceback

#---------------------------------------------------------------------------------------------------------#
def  AlignSequences (TracebackMatrix, sequence1, sequence2):
    """
    Aligns the two sequences according to the traceback matrix.
    -TracebackMatrix: Matrix where each cell indicates where score was from
    -sequence1: Same sequence for creating the traceback matrix
    -sequence2: Same sequence for creating the traceback matrix
    -returns: alignment1 and alignment2
    """

    i=len(sequence1)
    j=len(sequence2)

    alignment1 = list()
    alignment2 = list()
    
    # The traceback starts in the lower right corner of the tracebackmatrix. Numbers 1,2,3 in each cell 
    # reperesent from which adjustant cell the max score was calculated.
    while i != 0 or j != 0:                                                        
        if TracebackMatrix[i, j] == 1:
            alignment1.append(sequence1[i-1])
            alignment2.append(sequence2[j-1])
            i -= 1
            j -= 1
        elif TracebackMatrix[i, j] == 2:
            alignment1.append(sequence1[i-1])
            alignment2.append("_")
            i -= 1
        else:
            alignment1.append("_")
            alignment2.append(sequence2[j-1])
            j -= 1
   
    alignment1.reverse()
    alignment2.reverse()
    alignment1=''.join(alignment1)
    alignment2=''.join(alignment2)
    return alignment1, alignment2
    
#---------------------------------------------------------------------------------------------------------#
def AlignByDP(labelSequenceList):
    """
    Creates aligned sequences with given sequences from a list.
    -labelSequenceList: List with a label and according sequence in a tuple.
    -returns: Dictionary with two numbers (first and second label of input) as keys and the alignments
    as values.
    """
    
    InputCheck(labelSequenceList)
    
    # The KeyMermorizer stores the dictionary keys and its reverse (eg. 1,2 -> 2,1) if the alignment
    # has already been created it wont repeat the same pair again.
    alignedSequencesDict = dict()
    KeyMemorizer = list()

    for i in range(len(labelSequenceList)):
        for j in range(len(labelSequenceList)):
            key=i+1,j+1
            if i != j and key not in KeyMemorizer:            
                KeyMemorizer.append(key)
                KeyMemorizer.append(key[::-1])
                value = AlignSequences(TracebackMatrix(labelSequenceList[i][1],labelSequenceList[j][1]),
                                                       labelSequenceList[i][1],labelSequenceList[j][1])              
                alignedSequencesDict[key]=value
            continue
    return (alignedSequencesDict)

