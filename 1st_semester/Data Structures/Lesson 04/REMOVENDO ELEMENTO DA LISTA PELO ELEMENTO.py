lista = [1, 2, 6, 8, 3, 9, 90, 14, 500]
print(lista)

while True:
    elemento_remover=int(input("Digite o elemento que deseja remover da lista: "))
    if elemento_remover in lista:
        lista.remove(elemento_remover)
        print("Elemento removido com sucesso.")
        print (lista)
    else:
        print("Elemento não encontrado.")
        break