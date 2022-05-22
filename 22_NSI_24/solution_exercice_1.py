def maxliste(tab: list) -> int:
    valeur = tab[0]
    for element in tab:
        valeur = element if element > valeur else valeur
    return valeur


assert maxliste([98, 12, 104, 23, 131, 9]) == 131
assert maxliste([-27, 24, -3, 15]) == 24
