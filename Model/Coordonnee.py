# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0

def construireCoordonnee(li :int, co :int)->tuple:
    '''
    la fonction retourne un tuple qui contient le num de ligne et le num de colonne passés en paramètre
    '''
    if type(li) != int or type(li) != int :
        raise TypeError(f"construireCoordonnee : Le numéro de ligne {type(li)} ou le numéro de colonne {type(co)} ne sont pas des entiers")
    elif li < 0 or co < 0 :
        raise ValueError(f"construireCoordonnee : Le numéro de ligne {li} ou de colonne {co} ne sont pas positifs")
    else:
        res = (li,co)
        return res

def getLigneCoordonnee(coord:tuple):
    '''
    retourne le numéro de ligne de la coordonnée passée en paramètre
    '''
    if type(coord) != tuple:
        raise TypeError("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    else:
        return coord[0]
def getColonneCoordonnee(coord:tuple):
    '''
    retourne le numéro de colonne de la coordonnée passée en paramètre
    '''
    if type(coord) != tuple :
        raise TypeError("getColonneCoordonnee : Le paramètre n’est pas une coordonnée")
    else:
        return coord[1]

