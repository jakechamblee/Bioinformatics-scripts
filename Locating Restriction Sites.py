"""
A DNA string is a reverse palindrome if it is equal to its reverse complement.
For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12.
You may return these pairs in any order.
"""
test = 'TCAATGCATGCGGGTCTATATGCAT'
string = '''GCGCCGCTCTATAGGGATCACAAAAAAATACGATGAGAATGTCACAAAATATTCTTATGGAGTCTTTCCC
GGACCCCTATCCTTTACAACAACAGATCTGAGCCGGTCGCTCTTCGCGAGCGAAGGAACGTACGCAATATTAGCTTACGTAGGAACGACTAAGAACTTTACGACTACTCCGTTTGTTTCGGGCGTCGAATGAGGTGTCGTTACACATGTAGATGTGGGCGCACTACCAACACTATCTGCTGTAAGCGTTACAAATCAAGCAAAGTATATAACCCTGACCATAACCATGTAAAAGCCTCCGTGGTCTGGGTAGAAGGAGCAAATCCAAGAGGGGACGGCTAGTGTTCCGTGGAAAGCTTGAAGAGATCTGGTGGTAACCCATAGAACATTTTCTGACAACATGCGGCTGCAGCCGTGCGCCGCTTTAGTCTGGACATTCAAAACAAGTCGAGCCCGTTCACCTCCCTGGACGCCCTTCTACTGACTTGTTAACAATATCAGGTCGGGAACCGTGCGCTTGAAATGATCGGCGGAGGCTGTGACGCATGCAATCAACGTAACCGTGAAGGGGCGGAACGATCTTTTTATGCAACGCATATCGACGACCAAGACTAAATCCGTCAACGCAAATATCTTTTCGAGTTGTACTACGATCGGTTGTTTCTCTCTACCATAGTCGAGGGCGGACGGAGATACGGATGATTTAATCTTTAAACGGATGATGATGGTGAGTTCCCTAAATGCCTTACAGGATCGGCTCCTAAGCGAAGACATGAGCCTACTATTTCGACCGACGCGAATCCTATGTCGGAGCTATCCAAACTATA'''
from reverse_complement import rev_complement

def restriction_sites(dna):
    '''Searches the string for reverse palindromes from 4:12 nt long, at each base. Then moves to the next base.'''

    end = [4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in end:
        start = 0
        length = i
        for nucleotide in dna:
            # want to stop this loop when i distance from the end of the string
            # so find len(string) - i and when start reaches this number, stop the loop
            while start <= (len(dna)-length):
                if dna[start:i] == rev_complement(dna[start:i]):
                    print(start+1, length)
                start += 1
                i += 1


if __name__ == '__main__':
    print(restriction_sites(test))
# returns in 0.0127 seconds