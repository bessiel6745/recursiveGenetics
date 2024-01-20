"""
Authors: Bessie Li and Dika KC
Consulted: Suzy Xu
Date:12/5/23
Purpose: manipulates strings of 'A', 'C', 'U', 'T', and 'G' letters
    representing DNA and RNA base pairs, using recursion.
"""


#---------------#
# Provided Code #
#---------------#

def templateBase(base):
    """
    Given an RNA base ('A', 'U', 'G', or 'C') this function returns the
    DNA base that serves as a template for that base ('T' for 'A', 'A'
    for 'U', 'C' for 'G', and 'G' for 'C').
    """
    if base == 'A':
        return 'T'
    elif base == 'U':
        return 'A'
    elif base == 'G':
        return 'C'
    elif base == 'C':
        return 'G'
    else:
        raise ValueError("{} is not a valid RNA base!".format(repr(base)))


#-----------#
# Your Code #
#-----------#

def countOtherBases(seq, exclude):
    """returns the amount of bases excluding the excluded parameter"""
    if len(seq) == 0:
        return 0
    else:
        if seq[0] != exclude:
            return 1+ countOtherBases(seq[1:], exclude)
        else:
            return countOtherBases(seq[1:], exclude)
    
def templateSequence(seq1):
    """returns the dna base that was used as the template for the rna"""
    if seq1 == "":
        return ""
    else:
        x = templateBase(seq1[0])
        return x + templateSequence(seq1[1:])

def onlyAU(seq2):
    """returns the sequence with just A and U bases"""
    if seq2 == "":
        return ""
    else:
        if seq2[0] == "A" or seq2[0] == "U":
            return seq2[0] + onlyAU(seq2[1:])
        return onlyAU(seq2[1:])
    
def transcriptionErrors(seqrna, seqdna):
    """returns number of differences between the dna and rna"""
    if len(seqrna) == 0:
        return 0
    else:
        if templateBase(seqrna[0]) != seqdna[0]:
            return 1 + transcriptionErrors(seqrna[1:], seqdna[1:])
        else:
            return transcriptionErrors(seqrna[1:], seqdna[1:])


