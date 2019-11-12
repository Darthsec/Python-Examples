digito = int(input("Digite um número inteiro: "))
soma = 0
while digito > 0:
    resto = digito % 10
    digito = digito // 10
    soma = soma + resto
print(soma)