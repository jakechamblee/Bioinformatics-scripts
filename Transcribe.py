"""
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""
string = 'GATGGAACTTGACTACGTAAATT'


# note: this function assumes you are inputing a coding strand

def transcribe(dna):
    return dna.replace('T', 'U')


# from timeit import default_timer as timer
#
# start = timer()
if __name__ == '__main__':
    print(transcribe(string))
# end = timer()
# print(abs(start - end))
# returns in 1.6 x 10^-6 seconds
