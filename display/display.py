import os
import sys
from typing import Optional
from collections import deque

# ── Costanti muri ────────────────────────────────────────────────────────
NORTH = 1
EAST  = 2
SOUTH = 4
WEST  = 8

# ── Dimensioni pixel per cella e muro ────────────────────────────────────
CELL_PX = 4   # pixel per lato di ogni cella
WALL_PX = 1   # spessore muro in pixel

BG_COLOR   = (0,   0,   0)    # sfondo / muri
CELL_COLOR = (200, 200, 200)  # cella libera


COLOR_THEMES = [
    {   # tema 0: classico (come screenshot)
        "bg":      (0,   0,   0),
        "cell":    (200, 200, 200),
        "entry":   (180,  0, 180),
        "exit":    (200,  0,   0),
        "blocked": (100, 100, 100),
        "path":    (255, 220,   0),
    },
    {   # tema 1: scuro blu
        "bg":      (10,  10,  30),
        "cell":    (60,  80, 160),
        "entry":   (0,  200, 255),
        "exit":    (255,  60,  60),
        "blocked": (40,  40,  80),
        "path":    (0,  255, 160),
    },
    {   # tema 2: verde terminale
        "bg":      (0,   0,   0),
        "cell":    (0,  160,   0),
        "entry":   (0,  255, 100),
        "exit":    (255,  50,  50),
        "blocked": (0,   80,   0),
        "path":    (255, 255,   0),
    },
    {   # tema 3: sepia
        "bg":      (20,  12,   5),
        "cell":    (200, 170, 120),
        "entry":   (120, 200,  80),
        "exit":    (200,  60,  40),
        "blocked": (100,  80,  50),
        "path":    (255, 200,  80),
    },
]

RESET = "\033[0m"


def validate_walls(maze) -> bool:
    """in teoria gia' fatto con la generazione del labirinto"""
    pass


def _px(r: int, g: int, b: int) -> str:
    """Restituisce una coppia di spazi con background ANSI truecolor.
 
    Args:
        r, g, b: componenti RGB del colore.
 
    Returns:
        Stringa di 2 caratteri colorati + reset.
    """
    return f"\033[48;2;{r};{g};{b}m  {RESET}"
 

def render_maze(maze, theme_idx: int = 0) -> str:
    """Converte maze.grid in una stringa ANSI pronta per print().
 
    Args:
        maze: oggetto con width, height, grid (lista di liste di int).
 
    Returns:
        Stringa multi-riga con escape ANSI truecolor.
    """
    theme = COLOR_THEMES[theme_idx]
    wall = _px(*theme["bg"])
    cell = _px(*theme["cell"])
    entry = _px(*theme["entry"])
    exit_ = _px(*theme["exit"])
 
    lines = []
 
    for y in range(maze.height):
        """ogni riga di celle del labirinto occupa 2 righe di testo nel terminale."""

        row_a = ""  # angolo/muro NORTH  → larghezza: width*2 + 1 pixel
        row_b = ""  # muro WEST + cella  → larghezza: width*2 + 1 pixel
 
        for x in range(maze.width):
            c = maze.grid[y][x]
 
            # riga A: angolo (sempre muro) + muro NORTH o passaggio
            row_a += wall
            row_a += wall if (c & NORTH) else cell
 
            # riga B: muro WEST o passaggio + contenuto cella
            row_b += wall if (c & WEST) else cell
            if maze.entry == (x, y):
                row_b += entry
            elif maze.exit_ == (x, y):
                row_b += exit_
            else:
                row_b += cell
 
        # pixel finale a destra
        row_a += wall
        last = maze.grid[y][maze.width - 1]
        row_b += wall if (last & EAST) else cell
 
        lines.append(row_a)
        lines.append(row_b)
 
    # riga finale: chiude i muri SOUTH dell'ultima fila
    row_c = ""
    for x in range(maze.width):
        c = maze.grid[maze.height - 1][x]
        row_c += wall
        row_c += wall if (c & SOUTH) else cell
    row_c += wall

    lines.append(row_c)
 
    return "\n".join(lines)
 
 
if __name__ == "__main__":
    import os
 
    class FakeMaze:
        """5×4 con corridoio orizzontale sulla riga 0 e verticale sulla colonna 0."""
 
        # def __init__(self) -> None:
        #     self.width  = 5
        #     self.height = 4
        #     self.grid   = [[15] * self.width for _ in range(self.height)]
 

        def __init__(self) -> None:
            self.width = 10
            self.height = 10
            self.entry = (0, 0)
            self.exit_ = (9, 9)
            # ogni cella vale 15 = tutti i muri chiusi (0b1111)
            self.grid = [[15] * self.width for _ in range(self.height)]
 
            for x in range(self.width - 1):
                self.grid[0][x]   &= ~EAST
                self.grid[0][x+1] &= ~WEST
            for yy in range(self.height - 1):
                self.grid[yy][0]   &= ~SOUTH
                self.grid[yy+1][0] &= ~NORTH

    os.system("clear")
    print(render_maze(FakeMaze(), theme_idx=2))

