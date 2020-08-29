def consensus_seq(fastafile):
    """All passed sequences must be of the same length"""
    from Bio import SeqIO

    # Makes list of dna seq strings ['AGGC', ... 'CTAC']
    sequences = [str(seq.seq) for seq in SeqIO.parse(fastafile, "fasta")]
    profile = [{'A': 0, 'C': 0, 'G': 0, 'T': 0} for i in range(len(sequences[0]))]

    for seq in sequences:
        # Makes list of bases ['A','G','G'...] for each seq for enumerate()
        for position, base in enumerate([i for i in seq]):
            profile[position][base] += 1

    # The key argument describes how to compare the elements to get the max among them in the dictionary
    consensus = ''.join([max(profile[i], key=lambda k: profile[i][k]) for i in range(len(profile))])

    a_bases, c_bases = ' '.join([str(prof['A']) for prof in profile]), ' '.join([str(prof['C']) for prof in profile])
    g_bases, t_bases = ' '.join([str(prof['G']) for prof in profile]), ' '.join([str(prof['T']) for prof in profile])

    return print(consensus, f'\nA: {a_bases}', f'\nC: {c_bases}', f'\nG: {g_bases}', f'\nT: {t_bases}')


if __name__ == "__main__":
    consensus_seq("rosalind_cons.txt")
