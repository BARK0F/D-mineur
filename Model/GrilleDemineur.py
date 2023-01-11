# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True

def construireGrilleDemineur(li:int,co:int):
    '''
    retourne un tableau 2D régulier qui fera office de grille pour démineur
    '''
    if type(li)!=int or type(co)!=int:
        raise TypeError(f" construireGrilleDemineur : Le nombre de lignes {type(li)} ou de colonnes {type(co)} n’est pas un entier.")
    if li <= 0 or co <= 0 :
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes {li} ou de colonnes {co} est négatif ou nul.")
    tab = []
    for i in range(li):
        lst = []
        for j in range(co):
            lst.append(construireCellule())
        tab.append(lst)
    return tab

def getNbLignesGrilleDemineur(grille:list):
    '''
    retourne le nombre de ligne dans la grille du démineur
    '''
    if type_grille_demineur(grille)==False:
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)

def getNbColonnesGrilleDemineur(grille:list):
    '''
    retourne le nombre de colonne dans la grille du démineur
    '''
    if type_grille_demineur(grille)==False:
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille[0])

def isCoordonneeCorrecte(grille:list, coord:tuple)->bool:
    '''
    retourne si oui ou non la coordonnée passée en paramètre se trouve dans la grille passée en paramètre
    '''
    if type(grille)!=list or type(coord)!=tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type")
    res = True
    if getLigneCoordonnee(coord) < 0 or getLigneCoordonnee(coord) >= getNbLignesGrilleDemineur(grille):
        res = False
    elif getColonneCoordonnee(coord) < 0 or getColonneCoordonnee(coord) >= getNbColonnesGrilleDemineur(grille):
        res = False
    return res

def getCelluleGrilleDemineur(grille:list,coord:tuple):
    '''
    retourne la cellule se trouvant dans la grille passée en paramètre grâce aux coordonnée passée en paramètre
    '''
    if type(grille)!=list or type(coord)!=tuple:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type")
    if isCoordonneeCorrecte(grille,coord)==False:
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille")
    return grille[coord[0]][coord[1]]

def getContenuGrilleDemineur(grille:list,coord:tuple):
    '''
    retourne le contenue de la cellule se trouvant dans la grille passée en paramètre grâce aux coordonnée passée en paramètre
    '''
    con = getCelluleGrilleDemineur(grille,coord)
    return getContenuCellule(con)
def setContenuGrilleDemineur(grille:list,coord:tuple,contenu:int)->None:
    '''
    ne retourne rien, modifie le contenu de la cellule se trouvant aux coordonnée dans la grille
    '''
    con = getCelluleGrilleDemineur(grille,coord)
    setContenuCellule(con,contenu)
    return None

def isVisibleGrilleDemineur(grille:list,coord:tuple)->bool:
    '''
    retourne si la cellule se trouvant aux coordonée dans la grille est visible ou non
    '''
    con = getCelluleGrilleDemineur(grille,coord)
    return isVisibleCellule(con)

def setVisibleGrilleDemineur(grille:list,coord:tuple,vision:bool)->None:
    '''
    ne retourne rien, modifie la valeur de la visibilité de la cellule se trouvant dans la grille passée en paramètre
    '''
    con = getCelluleGrilleDemineur(grille,coord)
    setVisibleCellule(con,vision)
    return None

def contientMineGrilleDemineur(grille:list,coord:tuple)->bool:
    '''
    retourne True ou False si la cellule se trouvant aux coordonnée passées en paramètre contient une mine ou non
    '''
    con = getCelluleGrilleDemineur(grille,coord)
    return contientMineCellule(con)

def getCoordonneeVoisinsGrilleDemineur(grille:list,coord:tuple)->list:
    '''
    retourne une liste contenant les coordonnées des cellules voisines de la cellule se trouvant aux coordonnées passées en paramètre
    '''
    if type(grille)!=list:
        raise TypeError("getCoordonneeVoisinGrilleDemineur : un des paramètres n'est pas du bon type")
    if isCoordonneeCorrecte(grille,coord)==False:
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n'est pas dans la grille")
    res = []
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if x != 0 or y != 0:
                ligne = coord[0]+x
                colonne = coord[1]+y
                if 0 <= ligne < len(grille) and 0 <= colonne < len(grille[0]):
                    res.append((ligne,colonne))
    return res

def placerMinesGrilleDemineur(grille:list,nb:int,coord:tuple)->None:
    '''
    ne retourne rien, place aléatoirement des mines dans la grille sauf a la cellule dont les coord sont passées en paramètre
    '''
    if nb <= 0 or nb > (len(grille)*len(grille[0]))-1:
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    if isCoordonneeCorrecte(grille,coord)==False:
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n'est pas dans la grille")
    i = 0
    while i < nb:
        x = randint(0, getNbLignesGrilleDemineur(grille))
        y = randint(0, getNbColonnesGrilleDemineur(grille))
        cell = (x,y)
        if isCoordonneeCorrecte(grille,cell)==True:
            if getContenuGrilleDemineur(grille,cell) != const.ID_MINE and cell != coord:
                setContenuGrilleDemineur(grille,cell,const.ID_MINE)
                i += 1
    compterMinesVoisinesGrilleDemineur(grille)
    return None

def compterMinesVoisinesGrilleDemineur(grille:list)->None:
    '''
    ne retourne rien, compte le nombre de mine autour de chaque cellule qui ne contient pas de mine
    '''
    ligne = getNbLignesGrilleDemineur(grille)
    colonne = getNbColonnesGrilleDemineur(grille)
    for x in range(ligne):
        for y in range(colonne):
            cell = (x,y)
            if getContenuGrilleDemineur(grille,cell) != const.ID_MINE:
                mine = 0
                vois = getCoordonneeVoisinsGrilleDemineur(grille,cell)
                for i in vois:
                    if getContenuGrilleDemineur(grille,i) == const.ID_MINE:
                        mine += 1
                setContenuGrilleDemineur(grille,cell,mine)
    return None