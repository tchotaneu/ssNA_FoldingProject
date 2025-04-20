import random

BASES = ["A", "T", "G", "C"]
PAIRS = {"A": "T", "T": "A", "G": "C", "C": "G"}

def generate_random_sequence(length, gc_target=None):
    """
    Génère une séquence aléatoire d’ADN simple brin.
    :param length: longueur de la séquence
    :param gc_target: pourcentage de GC souhaité (ex : 50 pour 50%)
    :return: séquence ADN en string 
    """
    if gc_target is None:
        return ''.join(random.choices(BASES, k=length))
    
    gc_count = int(length * gc_target / 100)
    at_count = length - gc_count
    seq = random.choices("GC", k=gc_count) + random.choices("AT", k=at_count)
    random.shuffle(seq)
    return ''.join(seq)
