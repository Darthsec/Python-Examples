import math

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = (b ** 2) - 4 * a * c
print("Delta é",delta)

if delta < 0:
	print("Não há raiz real")
elif delta == 0:
	x = -b / (2 * a)
	print("X =", x)
elif	delta > 0:
	square = math.sqrt(delta)
	x1 = (-b + square) / (2 * a)
	x2 = (-b - square) / (2 * a)
	print("X1 =",x1 ,"X2 =",x2)
