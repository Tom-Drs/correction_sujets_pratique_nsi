def recherche(elt: int, tab: list) -> int:
    index = -1
    for index_element in range(len(tab)):
        if tab[index_element] == elt:
            index = index_element
    return index


assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(1, [1, 50, 1]) == 2
assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 5
