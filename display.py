import pygame  # ho scoperto che non si puo' usare pygame
from config import MazeConfig
# importare il MazeGenerator


# class FakeMaze:
#     def __init__(self) -> None:
#         self.width = 30
#         self.height = 30
#         self.entry = (0, 0)
#         self.exit_ = (9, 9)
#         # ogni cella vale 15 = tutti i muri chiusi (0b1111)
#         self.grid = [[15] * self.width for _ in range(self.height)]
        


CELL_SIZE = 20
WALL_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)

NORTH = 1
EAST  = 2
SOUTH = 4
WEST  = 8


def draw_maze(surface: pygame.Surface, maze: MazeConfig) -> None:
    """Disegna il labirinto sulla surface pygame.

    Args:
        surface: la finestra pygame su cui disegnare.
        maze: l'oggetto Maze con la griglia.
    """

    surface.fill(BG_COLOR)

    for y in range(maze.height):
        for x in range(maze.width):

            # pixel in alto a sx della cella corrente
            px = x * CELL_SIZE
            py = y * CELL_SIZE

            cell = maze.grid[y][x]

            if cell & NORTH:
                pygame.draw.line(
                    surface, WALL_COLOR, (px, py), (px + CELL_SIZE, py), 2
                )

            if cell & EAST:
                pygame.draw.line(
                    surface, WALL_COLOR, (px + CELL_SIZE, py), (px + CELL_SIZE, py + CELL_SIZE), 2
                )

            if cell & SOUTH:
                pygame.draw.line(
                    surface, WALL_COLOR, (px, py + CELL_SIZE), (px + CELL_SIZE, py + CELL_SIZE), 2
                )

            if cell & WEST:
                pygame.draw.line(
                    surface, WALL_COLOR, (px, py), (px, py + CELL_SIZE), 2
                )

    



def run_maze(maze: MazeConfig):
    """Avvia la finestra pygame e disegna il labirinto.

    Args:
        maze: l'oggetto Maze da visualizzare.
    """

    pygame.init()
    maze.grid[0][0] &= ~2   # rimuove bit EAST
    maze.grid[0][1] &= ~8   # rimuove bit WEST

    screen = pygame.display.set_mode(
        (maze.width * CELL_SIZE, maze.height * CELL_SIZE)
    )
    pygame.display.set_caption("A-Maze-ing")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
        draw_maze(screen, maze)
        pygame.display.flip()
    pygame.quit()




maze = MazeConfig()
run_maze(maze)