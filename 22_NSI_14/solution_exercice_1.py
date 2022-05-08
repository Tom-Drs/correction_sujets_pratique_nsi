def correspond(mot: str, mot_a_trous: str) -> bool:
    if len(mot) != len(mot_a_trous):
        return False
    for index in range(len(mot)):
        if not mot_a_trous[index] == "*" and mot[index] != mot_a_trous[index]:
            return False
    return True

assert correspond("INFORMATIQUE", "INFO*MA*IQUE") == True
assert correspond("AUTOMATIQUE", "INFO*MA*IQUE") == False