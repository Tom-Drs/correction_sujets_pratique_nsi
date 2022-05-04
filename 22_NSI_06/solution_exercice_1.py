def maxi(tab: list) -> tuple:
    maximum = (tab[0], 0)
    for index in range(len(tab)):
        if tab[index] > maximum[0]:
            maximum = (tab[index], index)
    return maximum


assert maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
