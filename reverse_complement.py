"""
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement of s.
"""
string = 'TAACGTCCCCCAGCCCAGATTCTGCTCGCCGTTAGAACCTGACGTACGTGATTCCCCATACGTCTGCGACTCTTCAGATCATGCAAAAGATCCCTCAACTCGTGCGAACGT' \
         'GCTGTGCACGGTTGGTTTGCTCAGCAGATCCGAACGCCTCACCACGTGGGGGTATTGCTAGTCCAAATCGCGTCATCAGAGTTTTAAACACTCAGATGGTTAGGGGGGCAC' \

def rev_complement(dna):
    # first reverse the string
    dna = dna[::-1]
    return dna.replace('T', 'a').replace('G', 'c').replace('A', 't').replace('C', 'g').upper()


# returns in 1.4 x 10^-5 seconds

if __name__ == '__main__':
    print(rev_complement(string))