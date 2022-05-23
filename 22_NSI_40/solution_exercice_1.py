def recherche(elt: int, tab: list) -> list:
    resultat = []
    for index in range(len(tab)):
        if tab[index] == elt:
            resultat.append(index)
    return resultat


assert recherche(3, [3, 2, 1, 3, 2, 1]) == [0, 3]
assert recherche(4, [1, 2, 3]) == []