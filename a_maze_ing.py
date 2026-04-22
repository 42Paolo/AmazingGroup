import sys
from config import ConfigError, parse_config
from mazegen import Maze

def main():
	if len(sys.argv) != 2:
		print("Usage: python a_maze_ing.py <config_file>")
		sys.exit(1)
	
	try:
		cfg = parse_config(sys.argv[1])
	except ConfigError as e:
		print(f"Error: {e}")
		sys.exit(1)

	maze = Maze(cfg.width, cfg.height, cfg.entry, cfg.exit_)
	#TODO andare a generare il labirinto
	#TODO controllare che le dimensioni siano > height/width rispetto alla raffigurazione del 42
	#non so, si potrebbe fare anche nel checker
if __name__ == "__main__":
	main()
