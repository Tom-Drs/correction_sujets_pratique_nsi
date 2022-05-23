def RechercheMin(tab: list) -> int:
    index = 0
    for index_element in range(len(tab)):
        if tab[index_element] < tab[index]:
            index = index_element
    return index


assert RechercheMin([5]) == 0
assert RechercheMin([2, 4, 1]) == 2
assert RechercheMin([5, 3, 2, 2, 4]) == 2