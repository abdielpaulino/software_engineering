def inserir_elemento(lista,elemento):
    lista.append(elemento)
    print('Elemento inserido com sucesso.')

def main():
    lista=[]
    while True:
        print('\n1-Inserir Elemento')
        print('0 -Encerrar o programa')
        opcao=input('Escolha uma opcao: ')

        if opcao=='1':
            elemento=input("Digite o elemento: ")
            inserir_elemento(lista,elemento)
        elif opcao=='0':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")

    print("Lista final: ", lista)
main()