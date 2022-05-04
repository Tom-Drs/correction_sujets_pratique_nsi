def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < len(seq_adn) and trouve == False:
        j = 0
        while j < g and gene[j] == seq_adn[i + j]:
            j += 1
        if j == g:
            trouve = True
        i += 1
    return trouve


assert recherche("AATC", "GTACAAATCTTGCC") == True
assert recherche("AGTC", "GTACAAATCTTGCC") == False
