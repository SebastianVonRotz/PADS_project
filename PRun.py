import P1
import P2
import P3
import P4

labelSequenceList = P1.ParseSeqFile("P1_sequences.txt")
print (labelSequenceList)

alignedSequencesDict = P2.AlignByDP(labelSequenceList)
print (alignedSequencesDict)

distMatrix = P3.ComputeDistMatrix(alignedSequencesDict)
print (distMatrix)

labelList = ["Mouse", "Bovine", "Gibbon", "Orangutan", "Gorilla", "Chimp", "Human"]
binaryTreeString = P4.Cluster(distMatrix, labelList)
print (binaryTreeString)


