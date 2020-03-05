'''Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs of s.
Strings can be returned in any order.'''
dna_strand = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'


def find_starts(strand, dna=True):
    '''This finds the indexes of all start codons in a string of RNA or DNA'''

    if dna:
        from Transcribe import transcribe
        strand = transcribe(strand)

    from Find_motif import find_motifs
    aug_indexes = find_motifs(strand, 'AUG')

    return aug_indexes


def open_reading_frames(strand, ignore_nested_orfs=False, ignore_duplicates=True):
    '''This function finds and translates all six potential open reading frames given ssDNA,
     and returns their peptide sequences'''
    from Transcribe import transcribe
    from translating_RNA import translate
    from reverse_complement import rev_complement

    strand = strand.rstrip('\n')  # removes newline characters often found in txt files
    opp_strand = transcribe(rev_complement(strand))
    strand = transcribe(strand)

    starts_strand, starts_opp_strand = find_starts(strand), find_starts(opp_strand, dna=False)  # returns start codon indexes
    orfs_strand = [strand[start:] for start in starts_strand]  # returns a list of nucleotide strings for each orf
    orfs_opp_strand = [opp_strand[start:] for start in starts_opp_strand]

    # now need logic which checks if any of these AUGs in the list are embedded within another reading frame
    # could transcribe, then translate, from AUG:stop for each start in the aug_indexes
    # if ignore_nested_orfs:

    protein_seqs = []
    for substring in orfs_strand:
        protein = translate(substring)
        if '_' in protein:
            index = protein.find('_')  # returns -1 if not found
            if index != -1:  # does not add reading frames which lack a stop codon (which occurs at end of a strand)
                protein_seqs.append(protein[:index])

    for substring in orfs_opp_strand:
        protein = translate(substring)
        if '_' in protein:
            index = protein.find('_')
            if index != -1:
                protein_seqs.append(protein[:index])

    if ignore_duplicates:
        protein_seqs = set(protein_seqs)

    return '\n'.join(protein_seqs)


if __name__ == '__main__':
    print(open_reading_frames(dna_strand))
