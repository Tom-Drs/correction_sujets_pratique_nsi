def moyenne(tab: list) -> float:
    somme = 0
    for element in tab:
        somme += element
    return somme / len(tab)

assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5