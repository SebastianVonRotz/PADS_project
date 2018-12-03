import P2
import numpy as np
from numpy import log

seqDict = P2.AlignByDP()

# testDict = {(1,2) : ("AAACATCCAAACACCA__ACCCCAG_", "ACCAAACCTGTCCCCATCTAACACCA"), (1,3) : ("AAACATCCAAAC_ACCAACCCCAG_", "AAT_ACCCAACTCGACCTACACCAA"), 
# (2,3) : ("ACCAAACCTGTCCCCATCTAACACCA", "A—ATACCCAACTCGACCTA-CACCAA")}

# type(testDict)

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
    dValue =  -3/4*log(1- (count / alignmentLength)*4/3)
    return dValue


def ComputeDistMatrix(alignedSeqDict):
    print (len(alignedSeqDict.keys()))
    distMatrix = np.zeros ((len(alignedSeqDict.keys()), len(alignedSeqDict.keys())))

    for key in alignedSeqDict:
        # print (key)
        # print (alignedSeqDict[key][0], alignedSeqDict[key][1])
        # print (EstimatedPdistance(alignedSeqDict[key][0], alignedSeqDict[key][1]))
        distMatrix[key[0]-1, key[1]-1]= round(EstimatedPdistance(alignedSeqDict[key][0], alignedSeqDict[key][1]), 3)
    # print (distMatrix)
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in distMatrix]))
    return distMatrix


ComputeDistMatrix(seqDict)


