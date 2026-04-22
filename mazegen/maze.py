class Maze:
	def __init__(self, width:int, height:int, entry: tuple[int, int], exit_: tuple[int, int]) -> None:
			self.width = width
			self.height = height
			self.entry = entry
			self.exit_ = exit_
			self.grid = [[0] * width for _ in range(height)]
	#BITWISE OPERATION
	def has_wall(self, x, y, direction):
		return bool(self.grid[y][x] & direction)

	def open_wall(self, x, y, direction):
		self.grid[y][x] &= ~direction

	def close_wall(self, x, y, direction):
		self.grid[y][x] |= direction

	def in_bounds(self, x, y):
		return 0 <= x < self.width and 0 <= y < self.height
                                                                                                  
#   Ricorda che ogni cella è un intero, e le direzioni corrispondono a bit:                         
#   - N = bit 0
#   - E = bit 1                                                                                     
#   - S = bit 2                                               
#   - W = bit 3
             
#  0  = nessuna parete                                                          
#   1  = N          ↑                                                            
#   2  = E            →                                         
#   3  = N+E        ↑ →
#   4  = S              ↓                                                        
#   5  = N+S        ↑   ↓
#   6  = E+S          → ↓                                                        
#   7  = N+E+S      ↑ → ↓                                                        
#   8  = W          ←
#   9  = N+W        ↑ ←                                                          
#   10 = E+W          → ←
#   11 = N+E+W      ↑ → ←                                                        
#   12 = S+W          ↓ ←                                                        
#   13 = N+S+W      ↑ ↓ ←
#   14 = E+S+W        → ↓ ←                                                      
#   15 = N+E+S+W    ↑ → ↓ ←  