print("WHILE")
lista_de_numeros = [1, 2, 3, 4, 5]
indice = 0
while indice < len(lista_de_numeros):
    numero = lista_de_numeros[indice]
    print(numero)
    indice += 1

print("\nFOR")
for numero in lista_de_numeros:
    print(numero)


print("\nBREAK")
for contador in range(1, 10):
    if contador % 2 == 0:
        break
    print(contador)


print("\nCONTINUE")
for contador in range(1, 10):
    if contador % 2 == 0:
        continue
    print(contador)
