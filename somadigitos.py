digito = int(input("Digite o digito a ser somado: "))
soma = 0
while digito > 0:
    resto = digito % 10
    digito = digito // 10
    soma = soma + resto
print("A Soma dos numeros é: ", soma)