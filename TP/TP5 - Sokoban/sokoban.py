from collections import deque, namedtuple
from copy import deepcopy
Joueur = "J"
Caisse = "C"
Espace = " "
Mur = "#"
Objectif = "O"

def verif_coords(map : list, pos : tuple):
    if pos[0] < 0 or pos[1] < 0:
        return False
    
    if pos[0] >= len(map) or pos[1] >= len(map[0]):
        return False

def est_joueur(map, pos):
    return verif_coords(map, pos) and map[pos[0]][pos[1]] == Joueur

def est_caisse(map, pos):
    return verif_coords(map, pos) and map[pos[0]][pos[1]] == Caisse



def UP(map, pos):
    if verif_coords(map,(pos[0]-1, pos[1])) and map[pos[0]-1][pos[1]] == Espace:
        #map[pos[0]-1][pos[1]] = Joueur
        #map[pos[0]][pos[1]] = Espace
        return True
    
    return False



    



def DOWN(map, pos):
    if verif_coords(map,(pos[0]+1, pos[1])) and map[pos[0]+1][pos[1]] == Espace:
        #map[pos[0]+1][pos[1]] = Joueur
        #map[pos[0]][pos[1]] = Espace

        return True
    return False
    

def LEFT(map, pos):
    if verif_coords(map,(pos[0], pos[1]-1)) and map[pos[0]][pos[1]-1] == Espace:
        #map[pos[0]][pos[1]-1] = Joueur
        #map[pos[0]][pos[1]] = Espace
        return True
    return False

def RIGHT(map, pos):
    if verif_coords(map,(pos[0], pos[1]+1)) and map[pos[0]][pos[1]+1] == Espace:
        #map[pos[0]][pos[1]+1] = Joueur
        #map[pos[0]][pos[1]] = Espace
        return True
    return False

def PUSH_UP(map, pos):
    if verif_coords(map,(pos[0]-1, pos[1])) and verif_coords(map, (pos[0]-2, pos[1])) and map[pos[0]-1][pos[1]] == Caisse and map[pos[0]-2][pos[1]] == Espace:
        #map[pos[0]-1][pos[1]] = Joueur
        #map[pos[0]-2][pos[1]] = Caisse
        #map[pos[0]][pos[1]] = Espace
        return True
    return False

def PUSH_DOWN(map, pos):
    if verif_coords(map,(pos[0]+1, pos[1])) and verif_coords(map, (pos[0]+2, pos[1])) and map[pos[0]+1][pos[1]] == Caisse and map[pos[0]+2][pos[1]] == Espace:
        #map[pos[0]+1][pos[1]] = Joueur
        #map[pos[0]+2][pos[1]] = Caisse
        #map[pos[0]][pos[1]] = Espace
        return True
    return False

def PUSH_LEFT(map, pos):
    if verif_coords(map,(pos[0], pos[1]-1)) and verif_coords(map, (pos[0], pos[1]-2)) and map[pos[0]][pos[1]-1] == Caisse and map[pos[0]][pos[1]-2] == Espace:
        #map[pos[0]][pos[1]-1] = Joueur
        #map[pos[0]][pos[1]-2] = Caisse
        #map[pos[0]][pos[1]] = Espace
        return True
    return False

def PUSH_RIGHT(map, pos):
    if verif_coords(map,(pos[0], pos[1]+1)) and verif_coords(map, (pos[0], pos[1]+2)) and map[pos[0]][pos[1]+1] == Caisse and map[pos[0]][pos[1]+2] == Espace:
        
        return True
    return False



def do_UP(map, pos):
    
    #map[pos[0]-1][pos[1]] = Joueur
    #map[pos[0]][pos[1]] = Espace
    return map

def do_DOWN(map, pos):
        
    #map[pos[0]+1][pos[1]] = Joueur
    #map[pos[0]][pos[1]] = Espace
    
    return map


def do_LEFT(map, pos):
        
    map[pos[0]][pos[1]-1] = Joueur
    map[pos[0]][pos[1]] = Espace
    return map

def do_RIGHT(map, pos):
            
    map[pos[0]][pos[1]+1] = Joueur
    map[pos[0]][pos[1]] = Espace
    return map

def do_PUSH_UP(map, pos):
            
    map[pos[0]-1][pos[1]] = Joueur
    map[pos[0]-2][pos[1]] = Caisse
    map[pos[0]][pos[1]] = Espace
    return map

def do_PUSH_DOWN(map, pos):
                
    map[pos[0]+1][pos[1]] = Joueur
    map[pos[0]+2][pos[1]] = Caisse
    map[pos[0]][pos[1]] = Espace
    return map

def do_PUSH_LEFT(map, pos):
                        
    map[pos[0]][pos[1]-1] = Joueur
    map[pos[0]][pos[1]-2] = Caisse
    map[pos[0]][pos[1]] = Espace
    return map

def do_PUSH_RIGHT(map, pos):
                                
    map[pos[0]][pos[1]+1] = Joueur
    map[pos[0]][pos[1]+2] = Caisse
    map[pos[0]][pos[1]] = Espace
    return map

Actions_possibles = [
    "UP",
    "DOWN",
    "LEFT",
    "RIGHT",
    "PUSH_UP",
    "PUSH_DOWN",
    "PUSH_LEFT",
    "PUSH_RIGHT",
]




def verif_plan(plan : list, map : list) -> bool:
    etat = deepcopy(map)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == Joueur:
                pos = (i,j)

    for action in plan:
        #Ajouter changement position joueur
        
        if action not in Actions_possibles:
            return False
        
        if action == "UP":
            if not UP(etat, pos):
                return False
            
            etat = do_UP(etat, pos)
            
            
            


        if action == "DOWN":
            if not DOWN(etat, pos):
                return False
            
            etat = do_DOWN(etat, pos)
            
            

        if action == "LEFT":
            if not LEFT(etat, pos):
                return False
            
            etat = do_LEFT(etat, pos)
            
            

        if action == "RIGHT":
            if not RIGHT(etat, pos):
                return False
            
            etat = do_RIGHT(etat, pos)
            
        

        if action == "PUSH_UP":
            if not PUSH_UP(etat, pos):
                return False
            
            etat = do_PUSH_UP(etat, pos)
            
            


        if action == "PUSH_DOWN":
            if not PUSH_DOWN(etat, pos):
                return False
            
            etat = do_PUSH_DOWN(etat, pos)
            
    

        if action == "PUSH_LEFT":
            if not PUSH_LEFT(etat, pos):
                return False
            
            etat = do_PUSH_LEFT(etat, pos)
            
            

        
        if action == "PUSH_RIGHT":
            if not PUSH_RIGHT(etat, pos):
                return False
            
            etat = do_PUSH_RIGHT(etat, pos)
            

        
    return True
    

Map = [
    [Mur, Mur, Mur, Mur, Mur, Mur, Mur, Mur],
    [Mur, Mur, Mur, Espace, Espace, Espace, Mur, Mur],
    [Mur, Objectif, Joueur, Caisse, Espace, Espace, Mur, Mur],
    [Mur, Mur, Mur, Espace, Caisse, Objectif, Mur, Mur],
    [Mur, Objectif, Mur, Mur, Caisse, Espace, Mur, Mur],
    [Mur, Espace, Mur, Espace, Objectif, Espace, Mur, Mur],
    [Mur, Caisse, Espace, Caisse, Caisse, Caisse, Objectif, Mur],
    [Mur, Espace, Espace, Espace, Objectif, Espace, Espace, Mur],
    [Mur, Mur, Mur, Mur, Mur, Mur, Mur, Mur]
]
Objectifs_pos = {(2,1), (3, 5), (4, 1), (5,4), (6, 7), (7,4)}



def etat_final(etat) -> bool:
    for i in range(len(etat)):
        for j in range(len(etat[0])):
            if etat[i][j] == Caisse and (i,j) not in Objectifs_pos:
                return False
            
    return True

def generate_neighboors(pos):
    neighboors = [(1, 0), (0,1), (-1,0), (0,-1)]


def bfs(map):
    """
        Fonction qui implémente un algorithme parcours d'abord.
    """
    file_attente = deque()
    etat = deepcopy(map)
    deplacements = ["UP", "DOWN", "LEFT", "RIGHT", "PUSH_UP", "PUSH_DOWN", "PUSH_LEFT", "PUSH_RIGHT"]
    visite = [[False for _ in range(len(map[0]))] for _ in range(len(map))]
    file_attente.append((x, y))

    # Recherche en largeur
    while file_attente:
        x, y = file_attente.popleft()

        
        
        # Explorer les différents actions
        for deplacement in deplacements:
            if deplacement == "UP":
                if UP(etat, (x,y)):
                    etat = do_UP(etat, (x,y))
                    file_attente.append((x-1, y))
                    visite[x-1][y] = True
                    if etat_final(etat):
                        return True, etat
                    #etat = deepcopy(map)
            if deplacement == "DOWN":
                if DOWN(etat, (x,y)):
                    etat = do_DOWN(etat, (x,y))
                    file_attente.append((x+1, y))
                    visite[x+1][y] = True
                    if etat_final(etat):
                        return True, etat
                    #etat = deepcopy(map)
            if deplacement == "LEFT":
                if LEFT(etat, (x,y)):
                    etat = do_LEFT(etat, (x,y))
                    file_attente.append((x, y-1))
                    visite[x][y-1] = True
                    if etat_final(etat):
                        return True, etat
                    #etat = deepcopy(map)
            if deplacement == "RIGHT":
                if RIGHT(etat, (x,y)):
                    etat = do_RIGHT(etat, (x,y))
                    file_attente.append((x, y+1))
                    visite[x][y+1] = True
                    if etat_final(etat):
                        return True, etat
                    #etat = deepcopy(map)
            if deplacement == "PUSH_UP":
                if PUSH_UP(etat, (x,y)):
                    etat = do_PUSH_UP(etat, (x,y))
                    file_attente.append((x-1, y))
                    visite[x-1][y] = True
                    if etat_final(etat):
                        return True, etat
                    #etat = deepcopy(map)
            if deplacement == "PUSH_DOWN":
                if PUSH_DOWN(etat, (x,y)):
                    etat = do_PUSH_DOWN(etat, (x,y))
                    file_attente.append((x+1, y))
                    visite[x+1][y] = True
                    if etat_final(etat):
                        return True, etat
                    #etat = deepcopy(map)
            if deplacement == "PUSH_LEFT":
                if PUSH_LEFT(etat, (x,y)):
                    etat = do_PUSH_LEFT(etat, (x,y))
                    file_attente.append((x, y-1))
                    visite[x][y-1] = True
                    if etat_final(etat):
                        return True, etat
                    #etat = deepcopy(map)

            if deplacement == "PUSH_RIGHT":
                if PUSH_RIGHT(etat, (x,y)):
                    etat = do_PUSH_RIGHT(etat, (x,y))
                    file_attente.append((x, y+1))
                    visite[x][y+1] = True
                    if etat_final(etat):
                        return True, etat
                    #etat = deepcopy(map)

    return False


def find_stg(map, stg):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == stg:
                return i, j

def succ(s, etat):
    """
        Fonction qui implémente un algorithme successeur.
    """

 
    successeurs = []
    if UP(etat, s):
        successeurs.append((s[0]-1, s[1]), "UP")
    if DOWN(etat, s):
        successeurs.append((s[0]+1, s[1]), "DOWN")
    if LEFT(etat, s):
        successeurs.append((s[0], s[1]-1), "LEFT")
    if RIGHT(etat, s):
        successeurs.append((s[0], s[0] + 1), "RIGHT")
    if PUSH_UP(etat, s):
        successeurs.append((s[0]-1, s[1]), "PUSH_UP")
    if PUSH_DOWN(etat, s):
        successeurs.append((s[0]+1, s[1]), "PUSH_DOWN")
    if PUSH_LEFT(etat, s):
        successeurs.append((s[0], s[1]-1), "PUSH_LEFT")
    if PUSH_RIGHT(etat, s):
        successeurs.append((s[0], s[1]+1), "PUSH_RIGHT")
    return successeurs

def action(s0, action, map):
    if action == "UP":
        return do_UP(map, s0)

def search_with_parent(
        map,
        s0,
        etat_final,
        succ,
):
    """
        Fonction qui implémente un algorithme de recherche avec parent.
    """
    etat = deepcopy(map)
    file_attente = [s0]
    save = {s0: None}
    file_attente.append(s0)

    while file_attente:
        s = file_attente.pop(0)
        if etat_final(s, etat):
            return True, save
        for s2 in succ(s):
            if s2 not in save:

                save[s2] = s
                file_attente.append(s2)
    return False, save

        

Position = namedtuple('Position', 'x y')
p1 = Position(0.0, 0.0)
p2 = Position(1.0, 1.0)
Test = {p1:1}
print(Test)
Test = {([[1,2]], 2):1}
print(Test)