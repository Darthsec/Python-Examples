n = int(input("Digite o valor de n: "))
impar = 0
while n > 0:
    impar = impar + 1
    if impar % 2 != 0:
        n = n - 1
        print(impar)