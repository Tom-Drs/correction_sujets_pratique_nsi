def delta(tab: list) -> list:
    tableau_resultat = [tab[0]]
    for index in range(1, len(tab)):
        tableau_resultat.append(tab[index] - tab[index - 1])
    return tableau_resultat


assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3]
assert delta([42]) == [42]
