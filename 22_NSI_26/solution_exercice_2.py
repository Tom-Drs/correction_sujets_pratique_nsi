def separe(tab):
    i = 0
    j = len(tab) - 1
    while i < j:
        if tab[i] == 0:
            i = i + 1
        else:
            tab[i], tab[j] = tab[j], tab[i]
            j = j - 1
    return tab


assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]