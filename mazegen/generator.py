import random
from .maze import Maze

PATTERN_42: list[tuple[int, int]] = [
	#vado a disegnare il 4 e il 2, sono le vairie cordiante, forse si puo fare piu piccolo coiscche il limite di grandezza sia
	#piu piccolo, ma sinceramente non e richeisto nel subject quindi non ne vedo la necessita
    (0, 0), (2, 0),
    (0, 1), (2, 1),
    (0, 2), (1, 2), (2, 2),
    (2, 3),
    (2, 4),
    (4, 0), (5, 0), (6, 0),
    (6, 1),
    (4, 2), (5, 2), (6, 2),
    (4, 3),
    (4, 4), (5, 4), (6, 4),
]

PATTERN_W = 7
PATTERN_H = 5
MIN_WIDTH = PATTERN_W + 2
MIN_HEIGHT = PATTERN_H + 2

class MazeGenerator:
    def __init__(self, maze: Maze, seed: int | None = None) -> None:
        self.maze = maze
        self.rng = random.Random(seed)

    def _place_42(self) -> bool:
        if self.maze.width < MIN_WIDTH or self.maze.height < MIN_HEIGHT:
            return False

        left_x = (self.maze.width - PATTERN_W) // 2
        top_y = (self.maze.height - PATTERN_H) // 2

        for col, row in PATTERN_42:
            x = left_x + col
            y = top_y + row
            if (x, y) == self.maze.entry or (x, y) == self.maze.exit_:
                continue
            self.maze.blocked.add((x, y))
            self.maze.grid[y][x] = 15

        return True

    def generate(self, algorithm: str = 'dfs', perfect: bool = True) -> None:
        has_pattern = self._place_42()
        if not has_pattern:
            print("Attenzione: labirinto troppo piccolo per disegnare il '42'")
			#non so se ci sono limitazioni precise

        if algorithm == 'prim':
            self._prim()
        else:
            self._dfs()
		#qua non so se bisogna fare un try, il mio praticamente ha 2 opzioni, se non e prim e usa in modo 
		#forzato dfs, P.S. nella classe ho messo 2 nominativi per dfs perche e lo stesso dfs e lo stesso di backtrace

        if not perfect:
            self._add_loops()
			#questa e per aggiungere dei collegamenti tra 2 percorsi vicini affiche ci siano piu soluzioni

	#check per l'ingressom, semplicemente vado a controllare se le cordinate dell'entrata si sovrappone a una cordinata del 42
	#nel caso fosse cosi va a cercare in tutto il labirinto la prima occorrenza di una cella che non sia bloccata e la returna
	#questo per mnon far crushare il programma
    def _get_start(self) -> tuple[int, int]:
        ex, ey = self.maze.entry
        if not self.maze.is_blocked(ex, ey):
            return (ex, ey)

        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if not self.maze.is_blocked(x, y):
                    return (x, y)

        return (0, 0)

    def _dfs(self) -> None:
        visited: set[tuple[int, int]] = set()
        start = self._get_start()
        stack = [start]
        visited.add(start)

        while stack:
            x, y = stack[-1]
			#lista delle celle ancora non visitate, solo cordinate, niente ogg
            unvisited: list[tuple[int, int, int, int]] = [] 
            for nx, ny, direction, opposite in self.maze.neighbors(x, y):
                if (nx, ny) not in visited:
                    unvisited.append((nx, ny, direction, opposite))

            if unvisited:
                nx, ny, direction, opposite = self.rng.choice(unvisited)
                self.maze.open_wall(x, y, direction)
                self.maze.open_wall(nx, ny, opposite)
                visited.add((nx, ny))
                stack.append((nx, ny))
            else:
                stack.pop()

	
    def _prim(self) -> None:
        visited: set[tuple[int, int]] = set()
        start = self._get_start()
        visited.add(start)

        frontier: list[tuple[int, int, int, int, int, int]] = []
        for nx, ny, direction, opposite in self.maze.neighbors(start[0], start[1]):
            frontier.append((start[0], start[1], direction, nx, ny, opposite))

        while frontier:
            i = self.rng.randrange(len(frontier))
            x, y, direction, nx, ny, opposite = frontier[i]
            frontier.pop(i)

            if (nx, ny) in visited:
                continue

            self.maze.open_wall(x, y, direction)
            self.maze.open_wall(nx, ny, opposite)
            visited.add((nx, ny))

            for nnx, nny, d, opp in self.maze.neighbors(nx, ny):
                if (nnx, nny) not in visited:
                    frontier.append((nx, ny, d, nnx, nny, opp))

	#questa e una funzione secondaria, serve soltnto nel caso perfect e false e quindi bisogna generare piu percorsi
	#quindi semplicmente vado a cercare una cella nella quale 2 blocchi dopo ci sia un'altra strada e vado a collegare le 2 strade
	#cosicche ci siano piu soluzioni
    def _add_loops(self) -> None:
        num_extra = max(1, (self.maze.width * self.maze.height) // 10)
        attempts = 0

        while num_extra > 0 and attempts < 500:
            attempts += 1
            x = self.rng.randrange(self.maze.width)
            y = self.rng.randrange(self.maze.height)

            if self.maze.is_blocked(x, y):
                continue

            neighbors = self.maze.neighbors(x, y)
            if not neighbors:
                continue

            nx, ny, direction, opposite = self.rng.choice(neighbors)
            if self.maze.has_wall(x, y, direction):
                self.maze.open_wall(x, y, direction)
                self.maze.open_wall(nx, ny, opposite)
                num_extra -= 1


# VEDO CHE CI SONO PIU' SOLOZIONI MA NON VENGONO MOSTRATE