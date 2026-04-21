class Maze:
	def __init__(self, width:int, height:int, entry: tuple[int, int], exit_: tuple[int, int]) -> None:
			self.width = width
			self.height = height
			self.entry = entry
			self.exit_ = exit_
			self.grid = [[0] * width for _ in range(height)]
	
	def has_wall(x, y, direction):
		pass

	def open_wall(x, y, direction):
		pass

	def close_wall(x, y, direction):
		pass

	def in_bounds(x, y):
		pass


# 	Perfetto. Prova a scrivere has_wall per primo — è il più semplice e gli altri si basano su di   
#   esso.                                                                                           
                                                                                                  
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