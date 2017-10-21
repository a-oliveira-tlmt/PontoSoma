class Point:
	
	def __init__(self, CoordX, CoordY):
		self.Px = CoordX
		self.Py = CoordY
		
	def __add__(self, Parc):
		PSoma = Point(0,0)
		PSoma.Px = self.Px + Parc.Px
		PSoma.Py = self.Py + Parc.Py
		return PSoma
	
	def __str__(self):
		return ("P(" + str(self.Px) + "," + str(self.Py) + ")")
		
