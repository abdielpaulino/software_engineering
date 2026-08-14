lista=[1,2,6,8,3,9,90,14,500]
print(lista)

elemento=int(input("Digite o elemento que deseja verificar: "))

if elemento in lista:
    print("Elemento encontrado.")
else:
    print("Elemento não encontrado.")