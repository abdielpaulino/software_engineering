lista = [1,2]
print(lista)

while True:
    posicao = int(input("Digite a posição que você quer inserir o elemento: "))
    elemento = int(input("Digite o elemento: "))

    if posicao > len(lista):
        print("Posição inválida.")
        break
    else:
        lista.insert(posicao, elemento)

    print (lista)
