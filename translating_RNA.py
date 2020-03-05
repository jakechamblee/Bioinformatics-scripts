'''
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.'''
string = '''AUGGGUUGCGGGCGGGUCUCAUCGGCUACCUUGUCCGUUUUUGUACAACCGUAUGGAGCAGGACAUCUGCGCGGCUGGUCCCAGUACCUUGCGUUAGUAUGCGUACCC
GCUCUAACCCGGGUAGCUAUUACGGGUCAUGUAGACUCGGUUUUACAGGUUGAAGCUGUGCCUAUUUACUUAACAAAUCCCACAGACCGCCAACUGACACACGGGUGUUUUGACCGGGUG
'''


def translate(rna):
    '''Must pass RNA strands which start with AUG to this function'''
    # note: this function does not break at stop codons, it simply adds an underscore

    codon_table = {
        'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
        'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
        'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
        'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
        'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
        'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
        'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
        'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
        'UAC': 'Y', 'UAU': 'Y', 'UAA': '_', 'UAG': '_',
        'UGC': 'C', 'UGU': 'C', 'UGA': '_', 'UGG': 'W', }
    start = 0
    end = 3
    protein_seq = []
    for i in range(len(rna)):
            if rna[start:end] in codon_table:
                protein_seq.append(codon_table[rna[start:end]])
            start += 3
            end += 3

    return ''.join(protein_seq)


if __name__ == '__main__':
    print(translate(string))