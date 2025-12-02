import os
import hashlib
from collections import defaultdict

def compute_hash(path, block_size=65536):
    """
    Vypočítá hash souboru (SHA256).
    Nejlepší metoda na určení duplicit podle obsahu.
    """
    sha = hashlib.sha256()

    try:
        with open(path, "rb") as f:
            while chunk := f.read(block_size):
                sha.update(chunk)
    except:
        return None  # soubor nejde přečíst

    return sha.hexdigest()


def find_duplicates_by_hash(results):
    """
    Najde duplicity podle hash.
    'results' zde musí být list tuple:
        (path, size, ext)
    Funkce dodá hash navíc a najde duplicity.
    """
    hash_map = defaultdict(list)

    for path, size, ext in results:
        h = compute_hash(path)
        if h:  # pokud se hash vypočítal
            hash_map[h].append(path)

    # Vrací jen ty hash skupiny, kde je víc než 1 soubor
    return {h: paths for h, paths in hash_map.items() if len(paths) > 1}
