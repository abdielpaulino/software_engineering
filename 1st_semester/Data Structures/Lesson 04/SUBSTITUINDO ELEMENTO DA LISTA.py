lista = [1,2]
print(lista)

posicao = int(input("Digite a posição que você quer inserir o elemento: "))
elemento = int(input("Digite o elemento: "))

while True:
    if posicao == len(lista):
        print("Posição inválida.")
    else:
        lista[posicao] = elemento

    print (lista)
    break