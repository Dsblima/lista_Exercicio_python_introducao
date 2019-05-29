# Escreva um programa que ordene uma lista numérica com três elementos.
lista = [10,7,9]
num1 = lista[0]
num2 = lista[1]
num3 = lista[2]

if num1 > num2:
    if num1 > num3:
        lista[2] = num1
        if num2 > num3:
            lista[0] = num3
            lista[1] = num2
        else:
            lista[0] = num2
            lista[1] = num3
    else:
        lista[0] = num2
        lista[1] = num1
        lista[2] = num3
elif num1 < num3:
    lista[0] = num1
    if num2 > num3:
        lista[1] = num3
        lista[2] = num2
    else:
        lista[1] = num2
        lista[2] = num3
else:
    lista[2] = num2
    lista[1] = num1
    lista[0] = num3

print(lista)



