def multiplication(n1: int, n2: int) -> int:
    resultat = 0
    for _ in range(abs(n1)):
        resultat += n2
    if n1 < 0:
        return -resultat
    return resultat


assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0
