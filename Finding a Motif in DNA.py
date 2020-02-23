"""
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""
string = 'CGGGTCGAGGGTCGAGGGTCGATGAGCCAGAAACTGGGTCGAATTGGGTCGAGGGTCGAGGTTGGGTCGACTAACGGGTCGAATTGGGTCGAGCCAGGGTCGACGGGTCGACTCTCACTGGGTCGAAAGCGGGGTC' \
         'GAGGGTCGACCTGGGGTCGAGTTCGGTATAGGGGTCGAGGAAGCGGGTCGAGGGTCGAGGGTCGAACCGGGGTCGACGGGTCGAGGGGTCGACCGACGGGTCGATAGGGTCGAATGGGGTCGAAGAGGATAGGGTC' \
         'GAGGGTCGACAGGGTCGAGGGTCGAAGGGTCGACAGCTCGGGTCGAGGGTCGAGGGTCGAGGGTCGAGGGTCGAGGGTCGAAGGCCGCGGGGTCGACCCGGGTCGAGCCCGGGTCGAGGGGTCGAGGGTCGAGGGG' \
         'GTCGACGGGGTCGATGGGGTCGATGCGTGGGTCGAGGGTCGACATGGGTCGAGCCTGGGTCGACGGGTCGAGGGTCGAGGGGGGTCGAGCCGGGTCGAGGGTCGAGTGGGTCGAGGGTCGAGGGTCGAGGGTCGAA' \
         'ATAGGGTCGAGGGTCGATTGGGTCGACCACAGGTCCCGGGTCGAGGGTCGATGTCGGGTCGAGGGGTCGACAGGGTCGATGCATAGGGTCGACGACGTATCGGGTCGAGGGGTCGAGGGTCGACGGGTCGAACCGT' \
         'CCGAGATGGGTCGATGGGTCGACGGGTCGAGGGTCGACGAGGGTCGAGGGTCGATGAAGGGTCGAGGGTCGAAAGGGTCGACACTGGGTCGACGGGTCGAGGGTCGAGCAGGGTCGACGGGTCGAGGGTCGAGGAG' \
         'GGGTCGAGGGTCGAGGGAAGGGTCGAGGGTCGACGGGGTCGATGGGTCGAGGGTCGAGGGGTCGAGGGGGTCGAGTTAGGGTCGATCCTAAAGGGTCGAGGGGGTCGACTCGGGTCGAGGGTCGAGGGTCGA'
mot = 'GGGTCGAGG'


def find_motifs(dna, motif):
    positions = []
    start = 0
    end = len(motif)

    for nucleotide in dna:
        if dna[start:end] == motif:
            positions.append(start + 1)
        start += 1
        end += 1
    return str(positions).replace(',', '')

# returns in 0.00025 seconds (2.5 x 10^-4 seconds)