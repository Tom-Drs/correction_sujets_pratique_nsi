def tri_bulles(T):
    n = len(T)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if T[j] > T[j + 1]:
                temp = T[j]
                T[j] = T[j + 1]
                T[j + 1] = temp
    return T


assert tri_bulles([123, 3, 4, 53, 12, 0, 234, 6]) == [0, 3, 4, 6, 12, 53, 123, 234]
