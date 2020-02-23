"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated;
"""
fasta = {}
with open('C:\\Users\jcham\AppData\Local\Temp\\rosalind_gc-1.txt', 'r') as file:
    for line in file:
        # remove \n characters
        line = line.strip()
        # skips blank lines
        if not line:
            continue
        # adds sequence name as key of the dictionary
        if line.startswith(">"):
            active_sequence_name = line[1:]
            if active_sequence_name not in fasta:
                fasta[active_sequence_name] = []
            continue
        fasta[active_sequence_name].append(line)

def gc_content(dictionary):
    # returns a dictionary of sequence names as keys with their nucleotide sequences as values
    gc_dict = {}
    for key, value in dictionary.items():
        # joining the list of lines from the txt file into one string for each sequence
        dictionary[key] = ''.join(value)
        gc_dict[key] = (dictionary[key].count('C') + dictionary[key].count('G')) / len(dictionary[key]) * 100
    return gc_dict

def highest_gc(dictionary):
    # returns a tuple with the name of the sequence with highest gc content in the dictionary, and its gc content
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key
    gcs = [dictionary[key] for key in dictionary]
    gcs.sort(reverse=True)
    highest = new_dict[gcs[0]]
    return highest, gcs[0]

print(gc_content(fasta)) # returns in 8.5 x 10^-5 seconds
print(highest_gc(gc_content(fasta))) # returns in 8.6x10^-5 seconds

