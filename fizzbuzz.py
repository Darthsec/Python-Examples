num_int = int(input("Digite o número inteiro: "))
div_5 = num_int % 3
div_3 = num_int % 5

if div_3 == 0 and div_5 == 0:
	print("FizzBuzz")
else:
	print(num_int)
