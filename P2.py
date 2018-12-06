"""
Title: Alignmen of Sequences
From: Sebastian von Rotz
Desription: The sequences from P1 are paired, so that each sequences is paired against each other once.
For each pair a Score Matrix with the corresponding traceback Matrix is created. The traceback Matrix is 
then used for the traceback which results in the alignment sequences of each pair.
"""
import P1
import numpy as np
#---------------------------------------------------------------------------------------------------------#
# def InputCheck ()

#---------------------------------------------------------------------------------------------------------#
def TracebackMatrix(sequence1, sequence2):
    array_zero = np.zeros ((len(sequence1)+1, len(sequence2)+1))
    array_traceback= np.zeros ((len(sequence1)+1, len(sequence2)+1))
    
    indel = -6
    match = 5
    mismatch = -2

    # Scoring array starts from 0, therefore -1 for correct character position
    def getScore(i,j):
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
    
    # Filling of the score Matrix and tracking of the max scores in a secon matrix for the traceback
    for i in range(1, len(sequence1)+1):
        for j in range(1, len(sequence2)+1):
            diagonal_score = array_zero[i-1, j-1] + getScore(i, j)
            upper_score = array_zero[i-1, j]+ indel
            left_score = array_zero[i, j-1] + indel
            array_zero[i,j] = max(diagonal_score, upper_score, left_score)

            if max(diagonal_score, upper_score, left_score) == diagonal_score:
                array_traceback[i, j] = 1
            elif max(diagonal_score, upper_score, left_score) == upper_score:
                array_traceback[i, j] = 2     
            else:
                array_traceback[i, j] = 3
    return array_traceback
#---------------------------------------------------------------------------------------------------------#
def  AlignedSequences (TracebackMatrix, sequence1, sequence2):
    i=len(sequence1)
    j=len(sequence2)

    alignment1 = list()
    alignment2 = list()
    
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
    print(alignment1)
    print(alignment2)
    return alignment1, alignment2
#---------------------------------------------------------------------------------------------------------#
def AlignByDP():
    pairs = P1.ParseSeqFile("P1_sequences.txt")
    print (pairs)  

    # The KeyMermorizer stores the dictionary keys and its reverse (eg. 1,2 -> 2,1).
    # If the alignment is already
    P2dict = dict()
    KeyMemorizer  =list()

    for i in range(len(pairs)):
        for j in range(len(pairs)):
            key=i+1,j+1
            if i != j and key not in KeyMemorizer:            
                print(key)
                KeyMemorizer.append(key)
                KeyMemorizer.append(key[::-1])
                value=AlignedSequences(TracebackMatrix(pairs[i][1],pairs[j][1]),pairs[i][1],pairs[j][1])              
                P2dict[key]=value
            continue
    return (P2dict)
