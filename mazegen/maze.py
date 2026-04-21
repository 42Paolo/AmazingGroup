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
             
#   Quindi per sapere se la parete Nord è chiusa, devi controllare se il bit 0 è a 1.         