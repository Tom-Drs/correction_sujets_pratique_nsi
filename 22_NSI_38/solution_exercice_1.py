
def tri_selection(tab: list) -> list:
    for i in range(len(tab)):
        mini = i
        for j in range(i, len(tab)):
            if tab[j] < tab[mini]:
                mini = j
        tab[i], tab[mini] = tab[mini], tab[i]
    return tab

assert tri_selection([1,52,6,-9,12]) == [-9, 1, 6, 12, 52]