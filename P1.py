"""
Title: Parsing a Sequence file
From: Sebastian von Rotz
Description: Through iterating a line and matching with regex expression, the name(label) of
the sequence and the sequence itself is returned in a new data structure, also the data check is 
included within the function.
"""
import re
#---------------------------------------------------------------------------------------------------------#
def ParseSeqFile(filepath):
        f=open(filepath)
        f=f.readlines()

        # regex is the regular expression, which has been defined on "https://regex101.com/" 
        # explanation can be read by putting the expression on the website
        regex = r"[>|>\s]([a-zA-Z]+)[\s|\t]+(.+)"
        regex2= r"[>]"

        pairs = list()
        for line in f:
                match = re.search(regex, line)
                no_data_match = re.search(regex2, line)

                if match :
                        groups = match.groups()
                        pairs.append(tuple([groups[0], groups[1].replace(" ", "")]))
                elif no_data_match :
                       raise RuntimeError("There is a line with a >, but no further data")
        return pairs