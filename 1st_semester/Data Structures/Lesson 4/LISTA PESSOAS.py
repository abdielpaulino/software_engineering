#COPIANDO DO SLIDE PG.14

import os
lista_pessoas = []

while True:
    nome = input("Informe o nome da pessoa (ou digite '0' para encerrar): ")
    if nome == '0':
        break

    idade = int(input("informe a idade da pessoa: "))
    cidade = input("Informe a cidade da pessoa: ")

    pessoa = {'nome': nome, 'idade': idade, 'cidade': cidade}
    lista_pessoas.append(pessoa)

    os.system('cls')
    print('\nLista de pessoas.')
    for pessoa in lista_pessoas:
        print(f'Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}')