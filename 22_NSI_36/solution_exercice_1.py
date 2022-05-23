def recherche(tab: list, n: int) -> int:
    if n not in tab:
        return len(tab)
    index_resultat = 0
    for index in range(len(tab)):
        if tab[index] == n:
            index_resultat = index
    return index_resultat


assert recherche([5, 3], 1) == 2
assert recherche([2, 4], 2) == 0
assert recherche([2, 3, 5, 2, 4], 2) == 3
