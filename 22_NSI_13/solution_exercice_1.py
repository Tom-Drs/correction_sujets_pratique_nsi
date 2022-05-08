def rendu(somme_a_rendre: int):
    n1 = 0
    n2 = 0
    n3 = 0
    while somme_a_rendre - 5 >= 0:
        n1 += 1
        somme_a_rendre -= 5
    while somme_a_rendre - 2 >= 0:
        n2 += 1
        somme_a_rendre -= 2
    while somme_a_rendre - 1 >= 0:
        n3 += 1
        somme_a_rendre -= 1
    return [n1, n2, n3]


assert rendu(13) == [2, 1, 1]
assert rendu(64) == [12, 2, 0]
assert rendu(89) == [17, 2, 0]
