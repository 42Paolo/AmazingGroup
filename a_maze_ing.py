import sys
from config import ConfigError, parse_config
from mazegen import Maze, MazeGenerator, solve_maze
from display.display import run_display


#prendo ogni cella la converto in hex e la scrvo nel file, successivamnete alla fine
#andro a scrivere come ultima linea il percorso per la soluzione, se non c'e scritto niente e perche non ce la soluzione
def write_output(maze: Maze, path: list[str] | None, output_file: str) -> None:
	with open(output_file, 'w') as f:
		for y in range(maze.height):
			row = ''.join(hex(maze.grid[y][x])[2:] for x in range(maze.width))
			f.write(row + '\n')
		f.write('\n')
		f.write(f"{maze.entry[0]},{maze.entry[1]}\n")
		f.write(f"{maze.exit_[0]},{maze.exit_[1]}\n")
		if path:
			f.write(''.join(path) + '\n')
		else:
			f.write('\n')


def main() -> None:
	if len(sys.argv) != 2:
		print("Usage: python a_maze_ing.py <config_file>")
		sys.exit(1)

	try:
		cfg = parse_config(sys.argv[1])
	except ConfigError as e:
		print(f"Error: {e}")
		sys.exit(1)
	except FileNotFoundError:
		print(f"Error: config file '{sys.argv[1]}' not found")
		sys.exit(1)

	maze = Maze(cfg.width, cfg.height, cfg.entry, cfg.exit_)
	algorithm = cfg.algorithm.value if cfg.algorithm else 'dfs'
	gen = MazeGenerator(maze, seed=cfg.seed)
	gen.generate(algorithm=algorithm, perfect=cfg.perfect)

	path = solve_maze(maze)
	if path is None:
		print("Attenzione: nessun percorso trovato tra entry e exit")

	try:
		write_output(maze, path, cfg.output_file)
		print(f"Labirinto salvato in '{cfg.output_file}'")
	except IOError as e:
		print(f"Errore nella scrittura del file: {e}")
		sys.exit(1)
	
	run_display(maze, algorithm=algorithm, perfect=cfg.perfect, path=path)


if __name__ == "__main__":
	main()
