def insere(a, tab):
    l = list(tab)  # l contient les mêmes éléments que tab
    l.append(a)
    i = len(l) - 2
    while a < l[i] and i >= 0:
        l[i + 1] = l[i]
        l[i] = a
        i = i - 1
    return l


assert insere(3, [1, 2, 4, 5]) == [1, 2, 3, 4, 5]
assert insere(10, [1, 2, 7, 12, 14, 25]) == [1, 2, 7, 10, 12, 14, 25]
assert insere(1, [2, 3, 4]) == [1, 2, 3, 4]
