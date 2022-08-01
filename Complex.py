"""
	Complex.py
	
	M. Reza Mozaffari
	Physics Group, University of Qom
"""

from math import *

class Complex ():
	def __init__ (self, x=0.0, y=0.0):
		self.x = float(x)
		self.y = float(y)
	
	def __str__ (self):
		if self.y < 0:
			return "{:.4f}-{:.4f}j".format(self.x, abs(self.y))
		else:
			return "{:.4f}+{:.4f}j".format(self.x, self.y)
			
	def __add__ (self, other):
		return Complex (self.x + other.x, self.y + other.y)
		
	def __sub__ (self, other):
		return Complex (self.x - other.x, self.y - other.y)	
	
	def __mul__ (self, other):
		if type(other) == type(self):
			return 	Complex (self.x*other.x - self.y*other.y, self.x*other.y + self.y*other.x)
		else:
			return 	Complex (self.x*other, self.y*other)

	def __rmul__ (self, scalar):
		return 	Complex (self.x*scalar, self.y*scalar)

	def conj (self):
		return Complex (self.x,-self.y)
	
	def __truediv__ (self, other):
		if type(other) == type(self):
			r2 = other.x*other.x + other.y*other.y
			C = self.__mul__ (other.conj())
			return Complex (C.x/r2, C.y/r2)
		else:
			return Complex (self.x/other, self.y/other)

	def __abs__ (self): 
		return 	sqrt(self.x*self.x + self.y*self.y)

	def radius (self): 
		return 	self.__abs__()
	
	def angle (self):
		return atan2(self.y,self.x)
	
	def __pow__ (self, other):
		if type(self) == type(other):
			C1 = Complex(log(self.radius()), self.angle())
			C2 = other.__mul__(C1)
			x2, y2  = C2.x, C2.y
			return Complex (exp(x2)*cos(y2), exp(x2)*sin(y2))
		else:
			r = self.radius()
			theta = self.angle()
			return Complex (r**other * cos(theta*other), r**other * sin(theta*other))

def power (a, other):
	C = Complex(other.x*log(a), other.y*log(a))
	x, y  = C.x, C.y
	return Complex (exp(x)*cos(y), exp(x)*sin(y))

def radius (other): 
	return 	other.radius()

def angle (other):
	return other.angle()
	
def logc (other):
	return Complex (log(radius(other)), angle(other))
