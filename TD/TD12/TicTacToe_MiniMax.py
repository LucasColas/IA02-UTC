from copy import deepcopy
from collections import namedtuple
#Player : str
#O player
#X player
#Actions
#Mark : namedtuple("Mark", ["mark", "coord"])
#State : set[Mark]
#Fonction terminale
#Next : prend un état et une action et un joueur et renvoie un état
#Fonction de gain : prend un état. Renvoie un float. 
#Goals : prend un état et un joueur et renvoie une liste d'action
#Action : tuple[int, int]

Mark = namedtuple("Mark", ["mark", "coord"])

def creer_etat_initial():
    return frozenset(Mark(" ", (i, j)) for i in range(3) for j in range(3))

def next(State, mark):
    updated_marks = []
    for m in State:
        if m.coord == mark.coord:
            updated_marks.append(mark)
        else:
            updated_marks.append(m)

    return frozenset(updated_marks)

def afficher_etat(State):
   
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            for mark in State:
                if mark.coord == (i, j):
                    print(mark.mark, end="|")
                    break
            else:
                print(" ", end=" ")
        print()

    print(" ", end=" ")
    for j in range(3):
        print(j, end=" ")

    print()
    
    
def jouer(State, currentPlayer):
    while True:
        i = int(input("i: "))
        j = int(input("j: "))
        for mark in State:
            if mark.coord == (i, j) and mark.mark == " ":
                State = next(State, Mark(currentPlayer, (i, j)))
                return State
        else:
           print("case occupée") 
    

def etat_terminal(State):
    """
    Renvoie True si toutes les marks ne sont plus " "
    Renvoie True si une ligne ou colonne ou diagonale est remplie par un joueur
    """

    # Check if a player won
    for i in range(3):
        if all(mark.mark == "X" for mark in State if mark.coord[0] == i):
            return True, "X"
        if all(mark.mark == "O" for mark in State if mark.coord[0] == i):
            return True, "O"
        if all(mark.mark == "X" for mark in State if mark.coord[1] == i):
            return True, "X"
        if all(mark.mark == "O" for mark in State if mark.coord[1] == i):
            return True, "O"
        
    # Check diagonal
    if all(mark.mark == "X" for mark in State if mark.coord[0] == mark.coord[1]):
        return True, "X"
    if all(mark.mark == "O" for mark in State if mark.coord[0] == mark.coord[1]):
        return True, "O"
    
    #Check anti diagonal
    if all(mark.mark == "X" for mark in State if mark.coord[0] + mark.coord[1] == 2):
        return True, "X"
    if all(mark.mark == "O" for mark in State if mark.coord[0] + mark.coord[1] == 2):
        return True, "O"


    return all(mark.mark != " " for mark in State), " "


def goals(State, player):
    """
    Renvoie une liste d'action possible
    """
    return [Mark(player, mark.coord) for mark in State if mark.mark == " "]

def evaluate(State, player):
    """
    fonction évaluation
    """
    res, res_joueur = etat_terminal(State)
    #print("res_joueur: ", res_joueur)
    #print("res: ", res_joueur)
    #print("player: ", player)

    if res_joueur == player:
        print("+1")
        return 1
    elif res_joueur == " ":
        #print("0")
        return 0
    #print("-1")
    return -1
    
    

def minimax(State, player, depth, Max):
    """
    Renvoie une action
    """
    res, res_joueur = etat_terminal(State)
    if res or depth == 0:
        eval = evaluate(State, player)
        if eval == 1 and player == "O":
            print("1. O won")
            afficher_etat(State)
        #print("eval: ", eval)
        return eval, None
    
    if Max:
        bestValue = float("-inf")
        bestAction = None
        #print("max : ", player)
        for action in goals(State, player):
            #print("action: ", action)
            #print("player: ", player)
            #print("depth: ", depth)
            #print("Max: ", Max)
            #print("next(State, action): ", next(State, action))
            #print("player: ", player)
            value, _ = minimax(next(State, action), "X" if player == "O" else "O", depth - 1, False)
            if value > bestValue:
                bestValue = value
                bestAction = action
        return bestValue, bestAction
    
    else:
        bestValue = float("inf")
        bestAction = None
        for action in goals(State, player):
            value, _ = minimax(next(State, action), "X" if player == "O" else "O", depth - 1, True)
            #print("value: ", value)
            if value < bestValue:
                bestValue = value
                bestAction = action
        return bestValue, bestAction

def main():
    State = creer_etat_initial()
    currentPlayer = "X"
    afficher_etat(State)
    while not etat_terminal(State)[0]:
        print(f"Player {currentPlayer} turn")
        if currentPlayer == "X":
            State = jouer(State, currentPlayer=currentPlayer)
        else:
            _, action = minimax(State, "O", 10, True)
            print("val : ", _)
            State = next(State, action)
        afficher_etat(State)
        #print("eval: ", evaluate(State, "X"))
        if etat_terminal(State)[0]:
            print(f"Player {currentPlayer} won")
        currentPlayer = "O" if currentPlayer == "X" else "X"



main()