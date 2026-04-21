import sys

from config import ConfigError, parse_config

def main():
	if len(sys.argv) != 2:
		print("Usage: python a_maze_ing.py <config_file>")
		sys.exit(1)
	
	try:
		cfg = parse_config(sys.argv[1])
	except ConfigError as e:
		print(f"Error: {e}")
		sys.exit(1)
	#TODO andare a generare il labirinto

if __name__ == "__main__":
	main()