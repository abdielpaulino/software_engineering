#Listas
lista_numeros = []
lista_pares = []
lista_impares = []

#Acumulador
i = 1

while True:
    num = int(input(f"Digite o {i} número:"))
    lista_numeros.append(num)
    if i == 5:
        break
    i += 1

for num in lista_numeros:
    if num % 2 != 0:
        lista_impares.append(num)

    else:
        lista_pares.append(num)

print ("Lista de todos os números:", lista_numeros)
print ("Lista dos números pares:", lista_pares)
print ("Lista dos números ímpares:", lista_impares)
