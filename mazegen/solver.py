from collections import deque
from .maze import Maze, DIR_LETTER

#prendo tutte le strade percorribili e le continuo a percorrere una cella alla volta, questo mi permette
#facendo cio appena una delle strade percorse trovera l'accesso alla stessa cordinata dell'uscita, abbiamo trovato 
#l'uscita come prima cosa ovviamente, ma secondariamente abbiamo anche per forza di cose il percorso piu veloce, dato
#che tutte le strade sono state percorse alla stessa velocita, spero capisci, senno ci si becca in call e te lo spiego
#mi sono fatto aiutare un po' da claude perche prima, le salvavo tutte, e successivamente facevo un controllo sulla lunghezza 
#del set di dati e quello piu corto lo returnavo, era abbastanza sporco come passaggi e in certe casistiche sbagliava, dato che
#andava a salvare anche i percorsi secondari sbaglaiti e prendeva quelli come giusti, era un po' un casino hahah, pero questa
#va bene
def solve_maze(maze: Maze) -> list[str] | None:
    start = maze.entry
    end = maze.exit_

    queue: deque[tuple[tuple[int, int], list[str]]] = deque()
    queue.append((start, []))

    visited: set[tuple[int, int]] = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path

        for nx, ny, direction, _opposite in maze.neighbors(x, y):
            if (nx, ny) not in visited and not maze.has_wall(x, y, direction):
                visited.add((nx, ny))
                new_path = path + [DIR_LETTER[direction]]
                queue.append(((nx, ny), new_path))

    return None
