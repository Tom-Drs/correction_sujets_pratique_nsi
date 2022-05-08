def moyenne(tab: list) -> float:
    if len(tab) == 0:
        return 'erreur'
    total = sum(tab)
    return total / len(tab)

assert moyenne([5,3,8]) == 5.333333333333333
assert moyenne([1,2,3,4,5,6,7,8,9,10]) == 5.5
assert moyenne([]) == 'erreur'
