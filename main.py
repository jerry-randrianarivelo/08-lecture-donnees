#### Imports et définition des variables globales
"""
Imports et définition des variables globales
"""
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    res = []
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()            # enlever espaces et \n
            if line:                       # ignorer les lignes vides
                numbers = [int(x) for x in line.split(';')]  # convertir chaque morceau en entier
                res.append(numbers)        # ajouter la sous-liste à res
    return res

def get_list_k(data, k):
    """
    Docstring pour get_list_k
    
    :param data: Description
    :param k: Description
    """
    return data[k]

def get_first(l):
    """
    Docstring pour get_first
    
    :param l: Description
    """
    return l[0]

def get_last(l):
    """
    Docstring pour get_last
    
    :param l: Description
    """
    return l[-1]

def get_max(l):
    """
    Docstring pour get_max
    
    :param l: Description
    """
    return max(l)

def get_min(l):
    """
    Docstring pour get_min
    
    :param l: Description
    """
    return min(l)

def get_sum(l):
    """
    Docstring pour get_sum
    
    :param l: Description
    """
    return sum(l)


#### Fonction principale


def main():
    """
    Docstring pour main
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
        k = 37
        print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
