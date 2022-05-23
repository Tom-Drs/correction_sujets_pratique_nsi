def moyenne(tab: list) -> float:
    somme = 0
    for valeur in tab:
        somme += valeur
    return somme / len(tab)

assert moyenne([1.0]) == 1.0
assert moyenne([1.0, 2.0, 4.0]) == 2.3333333333333335