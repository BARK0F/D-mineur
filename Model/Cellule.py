# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)



def isContenuCorrect(nb:int)->bool:
    '''
    retourne un booléen True si l'entier passé en paramètre est bien un entier et si il peut être le contenue d'une cellule
    '''
    return isinstance(nb,int) and 0<= nb <= 8 or nb == const.ID_MINE

def construireCellule(contenu:int=0, visible:bool=False):
    '''
    retourne un dictionnaire qui fera office de cellule
    '''
    if isContenuCorrect(contenu) == False:
        raise ValueError(f"construireCellule : le contenu {contenu} n’est pas correct")
    if type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre {visible} n’est pas un booléen")
    dic = {}
    dic[const.CONTENU] = contenu
    dic[const.VISIBLE] = visible
    return dic

def getContenuCellule(dic:dict)->int:
    '''
    retourne le contenu d'une cellule
    '''
    if type_cellule(dic)==False:
        raise TypeError("« getContenuCellule : Le paramètre n’est pas une cellule")
    return dic[const.CONTENU]

def isVisibleCellule(dic:dict)->bool:
    '''
    retourne si la cellule est visible ou pas
    '''
    if type_cellule(dic)==False:
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule")
    return dic[const.VISIBLE]

def setContenuCellule(dic:dict, contenu:int)->None:
    '''
    ne retourne rien, modifie avec le deuxième paramètre le contenue de la cellule
    '''
    if type_cellule(dic)==False:
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule")
    if type(contenu)!=int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier")
    if isContenuCorrect(contenu) == False:
        raise ValueError(f"setContenuCellule : la valeur du contenu {contenu} n’est pas correcte")
    dic[const.CONTENU] = contenu
    return None

def setVisibleCellule(dic:dict,bol:bool)->None:
    '''
    ne retourne rien, modifie avec le deuxième paramètre la visibilité de la cellule
    '''
    if type_cellule(dic)==False:
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule")
    if type(bol)!=bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen")
    dic[const.VISIBLE] = bol
    return None

def contientMineCellule(dic:dict)->bool:
    if type_cellule(dic)==False:
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule")
    if dic[const.CONTENU] == const.ID_MINE:
        bol = True
    else :
        bol = False
    return bol