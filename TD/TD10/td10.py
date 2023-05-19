from collections import deque

MAZE = [
    ["D", ".", ".", "."],
    [".", "W", ".", "W"],
    [".", "W", ".", "."],
    [".", "X", ".", "."],
]

#Parcours en largeur.
def get_neighbors(maze, current):
    neighbors = []
    x, y = current
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != "W":
            neighbors.append((nx, ny))
    return neighbors
def bfs(maze, start, end):
    queue = [start]
    visited = set()
    while queue:
        current = queue.pop(0)
        if current == end:
            return True
        visited.add(current)
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                queue.append(neighbor)
    return False

bfspath = bfs(MAZE, (3, 1), (0, 0))
print(bfspath)



def bfs_with_path(labyrinth, start, end):
    # Dimensions du labyrinthe
    rows = len(labyrinth)
    cols = len(labyrinth[0])

    # Vérification si la case de départ et la case d'arrivée sont valides
    if labyrinth[start[0]][start[1]] == 'W' or labyrinth[end[0]][end[1]] == 'W':
        return []

    # Liste des mouvements possibles (haut, bas, gauche, droite)
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # File d'attente pour le parcours en largeur
    queue = deque()
    queue.append(start)

    # Tableau pour suivre les cases visitées
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True

    # Tableau pour stocker le chemin
    path = [[None] * cols for _ in range(rows)]
    path[start[0]][start[1]] = start

    # Parcours en largeur
    while queue:
        current = queue.popleft()

        # Arrêt si la case actuelle est la case d'arrivée
        if current == end:
            break

        for movement in movements:
            next_row = current[0] + movement[0]
            next_col = current[1] + movement[1]

            # Vérification des limites du labyrinthe
            if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                continue

            # Vérification si la case suivante est une case valide et non visitée
            if labyrinth[next_row][next_col] != 'W' and not visited[next_row][next_col]:
                queue.append((next_row, next_col))
                visited[next_row][next_col] = True
                path[next_row][next_col] = current

    # Reconstruction du chemin
    if not visited[end[0]][end[1]]:
        return []

    path_list = []
    current = end
    while current != start:
        path_list.append(current)
        current = path[current[0]][current[1]]
    path_list.append(start)
    path_list.reverse()

    return path_list




path = bfs_with_path(MAZE, (3, 1), (0, 0))
if path:
    print("Chemin trouvé :")
    for row, col in path:
        print(f"({row}, {col})")
else:
    print("Aucun chemin trouvé.")

#Parcours en profondeur.
def dfs(maze, start, end):
    stack = [start]
    visited = set()
    while stack:
        current = stack.pop()
        if current == end:
            return True
        visited.add(current)
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                stack.append(neighbor)
    return False

def dfs_with_path(labyrinth, start, end):
    # Dimensions du labyrinthe
    rows = len(labyrinth)
    cols = len(labyrinth[0])

    # Vérification si la case de départ et la case d'arrivée sont valides
    if labyrinth[start[0]][start[1]] == 'W' or labyrinth[end[0]][end[1]] == 'W':
        return []

    # Liste des mouvements possibles (haut, bas, gauche, droite)
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Pile pour le parcours en profondeur
    stack = []
    stack.append(start)

    # Tableau pour suivre les cases visitées
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True

    # Tableau pour stocker le chemin
    path = [[None] * cols for _ in range(rows)]
    path[start[0]][start[1]] = start

    # Parcours en profondeur
    while stack:
        current = stack.pop()

        # Arrêt si la case actuelle est la case d'arrivée
        if current == end:
            break

        for movement in movements:
            next_row = current[0] + movement[0]
            next_col = current[1] + movement[1]

            # Vérification des limites du labyrinthe
            if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                continue

            # Vérification si la case suivante est une case valide et non visitée
            if labyrinth[next_row][next_col] != 'W' and not visited[next_row][next_col]:
                stack.append((next_row, next_col))
                visited[next_row][next_col] = True
                path[next_row][next_col] = current

    # Reconstruction du chemin
    if not visited[end[0]][end[1]]:
        return []

    path_list = []
    current = end
    while current != start:
        path_list.append(current)
        current = path[current[0]][current[1]]
    path_list.append(start)
    path_list.reverse()

    return path_list
path_dfs = dfs_with_path(MAZE, (3, 1), (0, 0))
if path_dfs:
    print("Chemin trouvé en DFS.")
    for row, col in path_dfs:
        print(f"({row}, {col})")
    
else:
    print("Aucun chemin trouvé en DFS.")
