def maxi(tab: list) -> tuple:
    plus_grand_element = (tab[0], 0)
    for index in range(len(tab)):
        if tab[index] > plus_grand_element[0]:
            plus_grand_element = (tab[index], index)
    return plus_grand_element


assert maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
