def conv_bin(n: int) -> tuple:
    binaire = []
    while n > 0:
        if n % 2 == 1:
            binaire.insert(0, 1)
        else:
            binaire.insert(0, 0)
        n = n // 2
    return (binaire, len(binaire))


assert conv_bin(9) == ([1, 0, 0, 1], 4)
