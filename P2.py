import P1
import numpy as np

pairs = P1.ParseSeqFile("P1_sequences.txt")
print (pairs)



def AlignByDP(pairs):

    def charToNumber(char):
        char_to_number = {"A":0, "C":1, "G":2, "T":3}
        return char_to_number[char]

    sequence1 = "TTCATA"
    sequence2 = "TGCTCGTA"

    seq_a = list(map(charToNumber, list(sequence1)))
    seq_b = list(map(charToNumber, list(sequence2)))

    Match = 5
    Mistmatch = -2
    Indel = -6

    #def array_initialization (seq1, seq2):
    array_zero = np.zeros ((len(seq_a)+1, len(seq_b)+1))
    # Scoring for Match and Mismatch
    scoring = np.array([[5,-2,-2,-2],
                        [-2,5,-2,-2],
                        [-2,-2,5,-2],
                        [-2,-2,-2,5]])

    def getScore(i,j):
        return scoring[seq_a[i-1], seq_b[j-1]] #Scoring array starts from 0, therefore -1 for correct position

    # Array computation
    for i in range(len(seq_a)+1):
        array_zero[i,0]=i*Indel

    array_zero
    for j in range(len(seq_b)+1):
        array_zero[0,j]=j*Indel

    array_zero
    for i in range(1, len(seq_a)+1):
        for j in range(1, len(seq_b)+1):
            array_zero[i,j] = max(array_zero[i-1, j-1] + getScore(i, j), array_zero[i-1, j]+ Indel, array_zero[i, j-1] + Indel)                                                       
    
    array_scored = array_zero
    array_scored


    number_to_char= {0:'A', 1:'C', 2:'G', 3:'T'}

   
    i=len(seq_a)
    j=len(seq_b)

    alignment1 = []
    alignment2 = []

    # comp 

    while i >0 and j>0:
        if array_scored[i-1,j-1] + getScore(i, j) == array_scored[i,j]:
            alignment1.append(number_to_char[seq_a[i-1]])
            alignment2.append(number_to_char[seq_b[j-1]])
            i -= 1
            j -= 1
        elif array_scored[i-1, j] + Indel == array_scored[i, 0]:
            alignment1.append(number_to_char[seq_a[i-1]])
            alignment2.append("_")
            i -= 1
        else:
            alignment2.append(number_to_char[seq_b[j-1]])
            alignment1.append("_")
            j -= 1

    while i > 0:
        alignment1.append(number_to_char[seq_a[i-1]])
        alignment2.append("_")
        i -= 1
    while j > 0:
        alignment2.append(number_to_char[seq_b[j-1]])
        alignment1.append("_")
        j -= 1

    alignment1.reverse()
    alignment1.reverse()
    print(alignment1)
    print(alignment2)


# P2dict=dict()
# def AlignByDP(pairs):
#     for i in range(len(pairs)):
#         for j in range(len(pairs)):
#             if i != j:
#                 key=i+1,j+1
#                 value=pairs[i][1],pairs[j][1]
#                 P2dict[key]=def AlignPair(i[1],j[1])
#             continue
#         return P2dict
