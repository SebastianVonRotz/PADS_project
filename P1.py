### Parsing a Sequence File

# Defining of the Imported Modules
import os
import re

def ParseSeqFile(filepath):

        # Changing the working directory (not necessary with Anaconda Python)
        #os.chdir(r"C:\Users\voro\OneDrive\9 Studium\1_Semester\Programming\Project")

        # Defining the functions

        f=open(filepath)
        f=f.readlines()
        regex = r"[>|>\s]([a-zA-Z]+)[\s|\t]+(.+)"
        regex2= r"[>]"
        # regex is the regular expression, which has been defined on "https://regex101.com/" 
        # explanation can be read by putting the expression on the website

        pairs = list()
        for line in f:
                match = re.search(regex, line)
                no_data_match = re.search(regex2, line)
                if match :
                        groups = match.groups()
                        pairs.append(tuple([groups[0], groups[1].replace(" ", "")]))
        #    else   Check for empty lines and/or lines with >but without Infos
                elif line == "\n":
                       raise RuntimeError("You should get ride of empty lines first")
                elif no_data_match :
                       raise RuntimeError("There is a line with a >, but no further data")
        print (pairs)

        return pairs