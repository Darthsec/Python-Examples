meuCartao = int(input ("Digite o numero de seu cartão de credito: "))
cartaoLido = 1
encontreiMeuCartao = False

while cartaoLido != 0 and not encontreiMeuCartao:
    cartaoLido = int(input ("Digite o numero do proximo cartão de credito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartao = True

if encontreiMeuCartao:
    print("Achei!")
else:
    print("Não achei!")
