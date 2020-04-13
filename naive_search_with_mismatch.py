def naive_mismatch(pattern, string, mismatch=0):
    '''Finds matches in a string by naive search
    :str pattern:
    :str genome:
    :int mismatch:
    :return: The first index of each match. Includes mismatches
    '''
    occurrences = []
    start = 0
    end = len(pattern)
    for i in range(len(string) - end + 1):
        # search: a list of tuples of matches for each character such that (char_pattern_1, char_1), etc
        search = list(zip(pattern, string[start:end]))
        differences = 0
        for j in range(len(search)):
            if search[j][0] != search[j][1]:
                differences += 1
        if differences <= mismatch:
            occurrences.append(i)
        start += 1
        end += 1
    return occurrences
