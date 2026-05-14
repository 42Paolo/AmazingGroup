import os
from .themes import COLOR_THEMES, RESET, THEME_NAMES
from mazegen.maze import Maze

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8


def _px(r: int, g: int, b: int) -> str:
    return f"\033[48;2;{r};{g};{b}m  {RESET}"


def _path_to_cells(maze: Maze, path: list[str]) -> set[tuple[int, int]]:
    cells: set[tuple[int, int]] = set()
    x, y = maze.entry
    cells.add((x, y))
    delta = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    for letter in path:
        dx, dy = delta[letter]
        x += dx
        y += dy
        cells.add((x, y))
    return cells


def render_maze(
    maze: Maze,
    theme_idx: int = 0,
    path_cells: set[tuple[int, int]] | None = None,
) -> str:
    theme_name = THEME_NAMES[theme_idx]
    theme = COLOR_THEMES[theme_name]
    wall_px = _px(*theme["bg"])
    cell_px = _px(*theme["cell"])
    entry_px = _px(*theme["entry"])
    exit_px = _px(*theme["exit"])
    blocked_px = _px(*theme["blocked"])
    path_px = _px(*theme["path"])

    def interior(x: int, y: int) -> str:
        if (x, y) == maze.entry:
            return entry_px
        if (x, y) == maze.exit_:
            return exit_px
        if maze.is_blocked(x, y):
            return blocked_px
        if path_cells and (x, y) in path_cells:
            return path_px
        return cell_px

    def passage(x1: int, y1: int, x2: int, y2: int) -> str:
        if path_cells and (x1, y1) in path_cells and (x2, y2) in path_cells:
            return path_px
        return cell_px

    lines = []

    for y in range(maze.height):
        row_a = ""
        row_b = ""

        for x in range(maze.width):
            c = maze.grid[y][x]

            row_a += wall_px
            if c & NORTH:
                row_a += wall_px
            elif y > 0:
                row_a += passage(x, y, x, y - 1)
            else:
                row_a += cell_px

            if c & WEST:
                row_b += wall_px
            elif x > 0:
                row_b += passage(x, y, x - 1, y)
            else:
                row_b += cell_px
            row_b += interior(x, y)

        row_a += wall_px
        last_c = maze.grid[y][maze.width - 1]
        row_b += wall_px if (last_c & EAST) else cell_px

        lines.append(row_a)
        lines.append(row_b)

    row_c = ""
    for x in range(maze.width):
        c = maze.grid[maze.height - 1][x]
        row_c += wall_px
        row_c += wall_px if (c & SOUTH) else cell_px
    row_c += wall_px
    lines.append(row_c)

    return "\n".join(lines)


def run_display(
    maze: Maze,
    algorithm: str = 'dfs',
    perfect: bool = True,
    path: list[str] | None = None,
    theme_idx: int = 0,
) -> None:

    from mazegen.maze import Maze
    from mazegen.generator import MazeGenerator
    from mazegen.solver import solve_maze

    show_path = False
    path_cells: set[tuple[int, int]] = (
        _path_to_cells(maze, path)
        if path
        else set()
    )

    os.system("clear")
    print(render_maze(maze, theme_idx, path_cells if show_path else None))

    running = True
    while running:
        print("\n1. Re-generate a new path")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")

        choice = input("\nChoice? (1-4): ").strip()

        if choice == "1":
            new_maze = Maze(maze.width, maze.height, maze.entry, maze.exit_)
            gen = MazeGenerator(new_maze)
            gen.generate(algorithm=algorithm, perfect=perfect)
            path = solve_maze(new_maze)
            maze = new_maze
            path_cells = _path_to_cells(maze, path) if path else set()
            os.system("clear")
            # CAMBIATO FILE DI OUTPUT PER TESTARE LA FUNZIONE DI SCRITTURA,
            # PRIMA ERA "output.txt" E QUANDO RIGENERAVI IL MAZE NON CAMBIAVA
            from a_maze_ing import write_output
            write_output(maze, path, "maze.txt")
            print(render_maze(
                        maze,
                        theme_idx,
                        path_cells if show_path else None
                    ))

        elif choice == "2":
            show_path = not show_path
            os.system("clear")
            print(render_maze(
                        maze,
                        theme_idx,
                        path_cells if show_path else None
                    ))

        elif choice == "3":
            print("Temi disponibili:")
            for idx, name in enumerate(COLOR_THEMES.keys(), start=1):
                print(f"{idx}. {name}")
            try:
                new_theme = int(input("Seleziona tema: "))
                if 1 <= new_theme <= len(COLOR_THEMES):
                    theme_idx = new_theme - 1
                    os.system("clear")
                    print(render_maze(
                        maze,
                        theme_idx,
                        path_cells if show_path else None
                    ))
                else:
                    print("Indice tema non valido.")
            except ValueError:
                print("Input non valido: inserire un numero intero.")

        elif choice == "4":
            print("BYE!")
            running = False

        else:
            print("Scelta non valida, riprova.")


if __name__ == "__main__":
    # from mazegen.maze import Maze
    from mazegen.generator import MazeGenerator
    from mazegen.solver import solve_maze

    m = Maze(20, 15, (0, 0), (19, 14))
    gen = MazeGenerator(m, seed=42)
    gen.generate(algorithm='dfs', perfect=True)
    p = solve_maze(m)
    run_display(m, algorithm='dfs', perfect=True, path=p, theme_idx=2)
