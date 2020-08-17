def prob_allele_is_dominant(k, m, n):
    '''
    Assumes mendelian inheritance i.e. no segregation distortion / meiotic drive effects.
    '''

    # probability of getting a dominant child from each pair
    p_het_het_child = 0.25
    p_het_rec_child = 0.5
    p_rec_rec_child = 1
    total_pop = k + m + n

    p_het_het_parents = (m / total_pop) * ((m - 1) / (total_pop - 1))

    p_het_rec_parents = (m / total_pop) * (n / (total_pop - 1))
    p_rec_het_parents = (n / total_pop) * (m / (total_pop - 1))

    p_rec_rec_parents = (n / total_pop) * ((n - 1) / (total_pop - 1))

    # must calculate the probability of getting all combinations of parents which can yield rec offspring
    # then must multiply the prob of each parent combo by the prob of that combo producing a rec offspring
    p_dom = 1 - (p_het_het_parents * p_het_het_child +
                 p_het_rec_parents * p_het_rec_child +
                 p_rec_het_parents * p_het_rec_child +
                 p_rec_rec_parents * p_rec_rec_child
                 )

    return p_dom

if __name__ == "__main__":
    print(prob_allele_is_dominant(2, 2, 2))