decrescente = True
anterior = int(input("Digite o primeiro Número da seguencia: "))
valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite o proximo numero da sequencia: "))
    if valor > anterior:
        decrescente = False
    anterior = valor
if decrescente:
    print("A seguencia está em ordem decrescente :-)")
else:
    print("A seguencia não está em ordem decrecente :-(")
