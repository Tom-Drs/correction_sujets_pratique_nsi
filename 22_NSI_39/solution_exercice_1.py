def moyenne(tab: list) -> float:
    somme = 0
    for element in tab:
        somme += element
    return somme / len(tab)

assert moyenne([10,20,30,40,60,110]) == 45.0