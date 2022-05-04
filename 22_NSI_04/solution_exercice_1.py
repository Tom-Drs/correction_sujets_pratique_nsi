def recherche(tab: list) -> list:
    tableau_resultat = []
    for index in range(1, len(tab)):
        if tab[index - 1] + 1 == tab[index]:
            tableau_resultat.append((tab[index - 1], tab[index]))
    return tableau_resultat


assert recherche([1, 4, 3, 5]) == []
assert recherche([1, 4, 5, 3]) == [(4, 5)]
assert recherche([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)]
assert recherche([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]
