lista = [1, 2, 6, 8, 3, 9, 90, 14, 500]
print(lista)

while True:
    posicao_remover=int(input("Digite o elemento que deseja remover da lista: "))
    if posicao_remover < 0 or posicao_remover >= len(lista):
        print ("Posição não encontrada.")
        break
    else:
        lista.pop(posicao_remover)
        print ("Elemento removido com sucesso.")
        print (lista)