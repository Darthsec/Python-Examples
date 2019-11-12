num_int = int(input("Digite o número inteiro: "))
div = num_int % 2

if div == 0:
	print("par")
elif div > 0:
	print("ímpar")
else:
	print(div)

