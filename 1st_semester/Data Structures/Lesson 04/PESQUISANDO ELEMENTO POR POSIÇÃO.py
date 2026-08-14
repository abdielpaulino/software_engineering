lista=[1,2,6,8,3,9,90,14,500]
print(lista)

posicao=int(input("Digite a posição do elemento que deseja verificar: "))

if 0 > posicao > len(lista):
    print("Posição inválida.")
else:
    print(lista[posicao])