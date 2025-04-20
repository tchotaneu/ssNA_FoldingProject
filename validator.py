def validate_structure(sequence, structure):
    """
    Évalue la correspondance d’une séquence à une structure secondaire simplifiée en notation dot-bracket.
    :param sequence: séquence ADN en string
    :param structure: notation dot-bracket en string exemple: "(((...)))"
    :return: nombre d'appariements valides, nombre total requis
    """
    stack = []
    valid_pairs = 0
    total_pairs = 0

    for i, char in enumerate(structure):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                j = stack.pop()
                total_pairs += 1
                if is_valid_pair(sequence[j], sequence[i]):
                    valid_pairs += 1

    return valid_pairs, total_pairs

def is_valid_pair(base1, base2):
    pairs = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return pairs.get(base1) == base2
