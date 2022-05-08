def recherche(tab: list, n: int) -> int:
    index_gauche = 0
    index_droit = len(tab) - 1
    while index_gauche <= index_droit:
        index_milieu = (index_droit + index_gauche) // 2
        if tab[index_milieu] == n:
            return index_milieu
        if tab[index_milieu] < n:
            index_gauche = index_milieu + 1
        else:
            index_droit = index_milieu - 1
    return -1


assert recherche([2, 3, 4, 5, 6], 5) == 3
assert recherche([2, 3, 4, 6, 7], 5) == -1
