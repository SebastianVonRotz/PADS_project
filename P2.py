#########Alignment of Sequence#########

######Defining of the Imported Modules######
import numpy as np
from numpy import array
from numpy import size
from numpy import dtype
from numpy import int16


######Defining the functions######
###First: Defining of the Sequences and the scores###


sequenz1 = "TTCATA"
char_to_number = {"A":0, "C":1, "G":2, "T":3}
sequence1_to_array = list()
for i in range(len(sequenz1)):
    sequence1_to_array.append(char_to_number[sequenz1[i]])
sequence1_to_array
seqi = array(sequence1_to_array)
seqi

sequenz2 = "TGCTCGTA"
char_to_number = {"A":0, "C":1, "G":2, "T":3}
sequence2_to_array = list()
for i in range(len(sequenz2)):
    sequence2_to_array.append(char_to_number[sequenz2[i]])
sequence2_to_array
seqj = array(sequence2_to_array)
seqj


Match = 5
Mistmatch = -2
Indel = -6

###Second: Creation of the Array###
#def array_initialization (seq1, seq2):
array_zero = np.zeros ((seqi.size+1, seqj.size+1))
#Scoring for Match and Mismatch
scoring = array([[5,-2,-2,-2],
                 [-2,5,-2,-2],
                 [-2,-2,5,-2],
                 [-2,-2,-2,5]])
def get_score(i,j):
    return scoring[seqi[i-1], seqj[j-1]] #Scoring array starts from 0, therefore -1 for correct position

#Array computation
for i in range(seqi.size+1):
    array_zero[i,0]=i*Indel
array_zero
for j in range(seqj.size+1):
    array_zero[0,j]=j*Indel
array_zero
for i in range(1, seqi.size+1):
    for j in range(1, seqj.size+1):
        array_zero[i,j] = max(array_zero[i-1, j-1] + get_score(i, j), array_zero[i-1, j]+ Indel, array_zero[i, j-1] + Indel)                                                       
array_scored = array_zero
array_scored

###Thrid: Traceback###

number_to_char= {0:'A', 1:'C', 2:'G', 3:'T'}

def get_aligned_pair(i,j):
    nucleotide1 = number_to_char[seqi[i-1]] if i>0 else "_"
    nucleotide2 = number_to_char[seqj[j-1]] if j>0 else "_"
    return (nucleotide1, nucleotide2)
 
i=seqi.size
j=seqj.size
alignment = []
while i >0 and j>0:
    if array_scored[[i-1, j-1]] + get_score(i, j) == array_scored[i,j]:
        alignment.append(get_aligned_pair(i, j))
    elif array_scored[i-1, j] + Indel == array_scored[i, 0]:
        alignment.append(get_aligned_pair(i, 0))
        i -= 1
    else:
        alignment.append(get_aligned_pair(0, j))
        j -= 1

while i > 0:
    alignment.append(get_aligned_pair(i, 0))
    i -= 1
while j > 0:
    alignment.append(get_aligned_pair(j, 0))
    j -= 1

alignment.reverse()
alignment
