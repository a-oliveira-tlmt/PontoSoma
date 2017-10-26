class Point:
	
	def __init__(self, CoordX, CoordY):
		self.Px = CoordX
		self.Py = CoordY
		
	def __add__(self, other):
		PSoma = Point(0,0)
		PSoma.Px = self.Px + other.Px
		PSoma.Py = self.Py + other.Py
		return PSoma
	
	def __eq__(self, other):
		isXEqual = self.Px == other.Px
		isYEqual = self.Py == other.Py
		return (isXEqual && isYEqual)
	
	def __str__(self):
		return ("P(" + str(self.Px) + "," + str(self.Py) + ")")
		
