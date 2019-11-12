

n = int(input("Digite o valor inteiro:"))
k = int(input("Digite a potencia:"))
i = 0
potencia = 1
while i < k:
	potencia = potencia * n
	i = i + 1
	print("O Valor de", n, "elevado a", k, "eh", potencia)
