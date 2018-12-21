"""
Title: Parsing a Sequence file
From: Sebastian von Rotz
Description: Through iterating a line and matching with regex expression, the name (label) of
the sequence and the sequence itself is returned in a new data structure.
"""
import re
#---------------------------------------------------------------------------------------------------------#
def InputCheck (labelSequenceList):
        """
        Raises exceptions if the Input is not correct.
        -labelSequenceList: list labels and sequences in tuples.
        -returns: None
        """
        if type(labelSequenceList) != list:
                raise RuntimeError("Data type is not a list")

        for part in range(len(labelSequenceList)):
                if type(labelSequenceList[part]) != tuple:
                        raise RuntimeError("Part of the list is not a tuple")

                elif type(labelSequenceList[part][0]) != str:
                        raise RuntimeError("Content of your tuple is not a string")
        
                elif type(labelSequenceList[part][1]) != str:
                        raise RuntimeError("Content of your tuple is not a string")

                elif (bool(re.search("^[ACTG]+$", labelSequenceList[part][1]))) != True:
                        raise RuntimeError("Second part a tuple does contain other characters than ATCG") 
        return None

#---------------------------------------------------------------------------------------------------------#
def ParseSeqFile(filepath):
        """
        Reads a file and creates two groups according to matches with regex expressions. Group one are the
        labels from sequences and group two are the sequences itself.
        -file:   name.txt file
        -return: list with tuples
        """

        f=open(filepath)
        f=f.readlines()

        # regex is the regular expression, which has been defined on "https://regex101.com/" 
        # explanation can be read by putting the expression on the website
        regex = r"[>|>\s]([a-zA-Z]+)[\s|\t]+(.+)"
        regex2= r"[>]"

        labelSequenceList = list()
        for line in f:
                match = re.search(regex, line)
                no_data_match = re.search(regex2, line)

                if match :
                        groups = match.groups()
                        labelSequenceList.append(tuple([groups[0], groups[1].replace(" ", "")]))
                elif no_data_match :
                       raise RuntimeError("There is a line with a >, but no further data")

        InputCheck(labelSequenceList)
        return labelSequenceList