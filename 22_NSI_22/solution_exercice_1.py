def renverse(mot: str) -> str:
    mot_inverse = ""
    for index in range(len(mot)-1, -1, -1):
        mot_inverse += mot[index]
    return mot_inverse


def renverse_flex(mot):
    return mot[::-1]


assert renverse("informatique") == "euqitamrofni"
assert renverse_flex("informatique") == "euqitamrofni"