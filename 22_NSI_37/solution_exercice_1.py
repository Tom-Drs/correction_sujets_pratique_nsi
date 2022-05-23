def verifie(tab: list) -> bool:
    for index in range(1, len(tab)):
        if tab[index-1] > tab[index]:
            return False
    return True

assert verifie([0, 5, 8, 8, 9]) == True
assert verifie([8, 12, 4]) == False
assert verifie([-1, 4]) == True
assert verifie([5]) == True