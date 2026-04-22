
W = 1  # su        ↑  (North - bit 0)
D = 2  # destra    →  (East  - bit 1)
S = 4  # giù       ↓  (South - bit 2)
A = 8  # sinistra  ←  (West  - bit 3)

DIR_LETTER: dict[int, str] = {W: "N", D: "E", S: "S", A: "W"}
class Maze:

	def __init__(
		self,
		width: int,
		height: int,
		entry: tuple[int, int],
		exit_: tuple[int, int],
	) -> None:
		self.width = width
		self.height = height
		self.entry = entry
		self.exit_ = exit_
		self.grid: list[list[int]] = [[15] * width for _ in range(height)]
		self.blocked: set[tuple[int, int]] = set() #questo mi serve per il disegno del 42

	def has_wall(self, x: int, y: int, direction: int) -> bool:
		return bool(self.grid[y][x] & direction)

	def open_wall(self, x: int, y: int, direction: int) -> None:
		self.grid[y][x] &= ~direction

	def close_wall(self, x: int, y: int, direction: int) -> None:
		self.grid[y][x] |= direction

	def in_bounds(self, x: int, y: int) -> bool:
		return 0 <= x < self.width and 0 <= y < self.height

	def is_blocked(self, x: int, y: int) -> bool:
		return (x, y) in self.blocked

	def neighbors(self, x: int, y: int) -> list[tuple[int, int, int, int]]:
		directions = [
			(x,     y - 1, W, S), 
			(x + 1, y,     D, A),  
			(x,     y + 1, S, W),  
			(x - 1, y,     A, D),  
		]
		return [
			(nx, ny, d, opp)
			for nx, ny, d, opp in directions
			if self.in_bounds(nx, ny) and not self.is_blocked(nx, ny)
		]
	#Per il 42 centrale
	def get_center(self) -> tuple[int, int]:                                                        
	  return self.width // 2, self.height // 2  
	#cx, cy = maze_get_centre

		
