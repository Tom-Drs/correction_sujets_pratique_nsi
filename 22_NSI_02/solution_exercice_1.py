def moyenne(notes: list) -> int:
    total_notes = 0
    total_coefficients = 0
    # J'utilise l'unpacking ici qui est très pratique car les éléments sont des tuples de deux valeurs.
    for note, coefficient in notes:
        total_notes += note * coefficient
        total_coefficients += coefficient
    return total_notes / total_coefficients


assert moyenne([(15, 2), (9, 1), (12, 3)]) == 12.5
