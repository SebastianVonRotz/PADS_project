import P1
import P2
import P3
import P4
import numpy as np

labelSequenceList = P1.ParseSeqFile("P1_sequences.txt")
print (labelSequenceList)

alignedSequencesDict = P2.AlignByDP(labelSequenceList)
print (alignedSequencesDict)

distMatrix = P3.ComputeDistMatrix(alignedSequencesDict)
print (distMatrix)

labelList = ["Mouse", "Bovine", "Gibbon", "Orangutan", "Gorilla", "Chimp", "Human"]

binaryTreeString = P4.Cluster(distMatrix, labelList)
print (binaryTreeString)

#Test P4
distMatrix = np.array([[0, 17, 21, 31, 23],
                      [17, 0, 30, 34, 21],
                      [21, 30, 0, 28, 39],
                      [31, 34, 28, 0, 43],
                      [23, 21, 39, 43, 0]])
 
labelList = ["a", "b", "c", "d", "e"]

binaryTreeString = P4.Cluster(distMatrix, labelList)
print (binaryTreeString)