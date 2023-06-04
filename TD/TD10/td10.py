from collections import deque
import heapq
MAZE = [
    ["D", ".", ".", "."],
    [".", "W", ".", "W"],
    [".", "W", ".", "."],
    [".", "X", ".", "."],
]
WALL = "W"
#Parcours en largeur.
def get_neighbors(maze, current):
    neighbors = []
    x, y = current
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != WALL:
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


def algorithme_glouton(maze, start, end):
    current = start
    path = [current]
    while current != end:
        neighbors = get_neighbors(maze, current)
        if not neighbors:
            return False, ()
        next = min(neighbors, key=lambda neighbor: manhattan_distance(neighbor, end))
        current = next
        path.append(current)
    return True, path


# Parcours en appronfondissement itératif
def iterative_deepening_dfs(maze, start, end):
    depth = 0
    while True:
        stack = [start]
        visited = set()
        while stack:
            current = stack.pop()
            if current == end:
                return True
            visited.add(current)
            if len(visited) > depth:
                continue
            for neighbor in get_neighbors(maze, current):
                if neighbor not in visited:
                    stack.append(neighbor)
        depth += 1
        if depth > len(maze) * len(maze[0]):
            return False
        

# Algorithme de l'escalade avec la distance de manhattan
def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def hill_climbing(maze, start, end):
    current = start
    path = [current]
    while current != end:
        neighbors = get_neighbors(maze, current)
        if not neighbors:
            return False, ()
        next = min(neighbors, key=lambda neighbor: manhattan_distance(neighbor, end))
        if manhattan_distance(next, end) >= manhattan_distance(current, end):
            return False, ()
        current = next
        path.append(current)
    return True, path




# Algorithme A*
def astar(start, goal, map):
    # Create dictionaries to store the costs and parents of each cell
    costs = {}
    parents = {}

    # Create a priority queue to store the cells to be explored
    queue = []
    heapq.heappush(queue, (0, start))
    costs[start] = 0
    movement_costs = [1, 1, 1, 1]
    movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        current_cost, current_cell = heapq.heappop(queue)

        if current_cell == goal:
            break

        for i, movement in enumerate(movements):
            new_cell = (current_cell[0] + movement[0], current_cell[1] + movement[1])

            if 0 <= new_cell[0] < len(map) and 0 <= new_cell[1] < len(map[0]) and map[new_cell[0]][new_cell[1]] != WALL:
                new_cost = current_cost + movement_costs[i]

                if new_cell not in costs or new_cost < costs[new_cell]:
                    costs[new_cell] = new_cost
                    priority = new_cost + manhattan_distance(new_cell, goal)
                    heapq.heappush(queue, (priority, new_cell))
                    parents[new_cell] = current_cell

    # Reconstruct the path from start to goal
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parents[current]
    path.append(start)
    path.reverse()

    return path



path_dfs = dfs_with_path(MAZE, (3, 1), (0, 0))
if path_dfs:
    print("Chemin trouvé en DFS.")
    for row, col in path_dfs:
        print(f"({row}, {col})")
    
else:
    print("Aucun chemin trouvé en DFS.")


path_bfs = bfs_with_path(MAZE, (3, 1), (0, 0))

if path_bfs:
    print("Chemin trouvé :")
    for row, col in path_bfs:
        print(f"({row}, {col})")
else:
    print("Aucun chemin trouvé.")


res, path = hill_climbing(MAZE, (3, 1), (0, 0))
print("res hill climbing",res)
print("path : ", path)

maze2 = [
    [".", ".", ".", "D"],
    [".", "W", "W", "W"],
    [".", "W", ".", "W"],
    [".", "X", ".", "W"],
]

res, path = hill_climbing(maze2, (3, 1), (0, 3))
print("res hill climbing",res)

path = astar((3, 1), (0, 0), MAZE)
print("path : ", path)