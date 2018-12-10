"""
Title: Pairwise Distance Matrix
From: Sebastian von Rotz
Desription: 
"""
import P2
import numpy as np
from numpy import log
from sympy.solvers import solve
from sympy import Symbol
#---------------------------------------------------------------------------------------------------------#
# def InputCheck ()


#---------------------------------------------------------------------------------------------------------#
def EstimatedPdistance (sequence1, sequence2):
    count=0
    alignmentLength=0
    for char in range(len(sequence1)):
        if sequence1[char] == "_" or sequence2[char] == "_":
            continue
        elif sequence1[char] == sequence2[char]:
            alignmentLength +=1
        else:
            count += 1
            alignmentLength +=1
    dValue =  -3/4*log(1- (count/alignmentLength)*4/3)
    return dValue

#---------------------------------------------------------------------------------------------------------#
def ComputeDistMatrix():
    seqDict = P2.AlignByDP()

    print (len(seqDict.keys()))
    x = Symbol('x', positive = True)
    a = len(seqDict.keys())
    matrixSideLength = solve(x**2 - x -2*a, x)
    
    distMatrix = np.zeros ((int(matrixSideLength[0]), (int(matrixSideLength[0]))))

    for key in seqDict:
        print (seqDict[key][0])
        print (seqDict[key][1])

        distMatrix[key[0]-1, key[1]-1]= round(EstimatedPdistance(seqDict[key][0], seqDict[key][1]), 5)
        distMatrix[key[1]-1, key[0]-1]= round(EstimatedPdistance(seqDict[key][0], seqDict[key][1]), 5)

    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in distMatrix]))
    return distMatrix




