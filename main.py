"""
	main.py
	
	M. Reza Mozaffari
	Physics Group, University of Qom
"""

from Complex import *

if __name__ == "__main__":

	C0 = Complex()
	print("C0 = ", C0)
	
	C1 = Complex(3.0, 3.0)
	print("C1 = ", C1)

	C0 = C1
	print("C0 = ", C0)
	
	C2 = Complex(1.0,-2.0)
	print("C2 = ", C2)

	print("C1 + C2 = ", C1 + C2)
	
	print("C1 - C2 = ", C1 - C2)
	
	print("C1 * C2 = ", C1 * C2)
	
	print("2.0 * C2 = ", 2.0 * C2)
	print("C2 * 2.0 = ", C2 * 2.0)

	print("C2 / C1 = ", C2 / C1)
	print("3.0 * C2 / 2.0 = ", 3.0 * C2 / 2.0)
	
	print("conj(C1) = ", C1.conj())
	print("C1 * conj(C1) = ", C1 * C1.conj())
	
	print("|C1| = ", abs(C1))
	print("C1 radius = ", C1.radius())
	print("C1 radius = ", radius(C1))
	print("C1 angle = ", C1.angle(), "rad.")
	print("C1 angle = ", angle(C1), "rad.")
	print("C1 angle = ", C1.angle()*180.0/pi, "deg.")
	
	C3 = Complex(2.0, 3.0)
	print("C3 = ", C3)
	print("C3**1.5 = ", C3**1.5)
	
	C4 = Complex(1.0, 1.0)
	print("C4 = ", C4)
	print("C3**C4 = ", C3**C4)
	
	print("2.0^C3 = ", power(2.0, C3))
	
	print("log(C3) = ", logc(C3))
