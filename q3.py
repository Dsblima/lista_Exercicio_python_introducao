#Escreva um programa que resolva uma equação de segundo grau.
a = int(input("Digite o valor do coeficiente a: "))
b =int( input("Digite o valor do coeficiente b: "))
c =int( input("Digite o valor do coeficiente c: "))

delta = b**2 - 4*a*c

if delta<0:
    print("Esta equação não possui raíz no conjunto dos números reais")
else:
    x1 = (-b+( delta ** (1/2) ))/ (2*a)
    x2 = (-b-( delta ** (1/2) ))/ (2*a)

    print("As raízes da equação são: ")
    print(x1)
    print(" e ")
    print(x2)