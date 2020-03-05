"""
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""
string = 'CGGGTCGAGGGTCGAGGGTCGATGAGCCAGAAACTGGGTCGAATTGGGTCGAGGGTCGAGGTTGGGTCGACTAACGGGTCGAATTGGGTCGAGCCAGGGTCGACGGGTCGACTCTCACTGGGTCGAAAGCGGGGTC' \
         'GAGGGTCGACCTGGGGTCGAGTTCGGTATAGGGGTCGAGGAAGCGGGTCGAGGGTCGAGGGTCGAACCGGGGTCGACGGGTCGAGGGGTCGACCGACGGGTCGATAGGGTCGAATGGGGTCGAAGAGGATAGGGTC' \
mot = 'GGGTCGAGG'


def find_motifs(dna, motif):
    positions = []
    start = 0
    end = len(motif)

    for nucleotide in dna:
        if dna[start:end] == motif:
            positions.append(start)
        start += 1
        end += 1
    return positions


if __name__ == '__main__':
    print(find_motifs(string,mot))
# returns in 0.00025 seconds (2.5 x 10^-4 seconds)
