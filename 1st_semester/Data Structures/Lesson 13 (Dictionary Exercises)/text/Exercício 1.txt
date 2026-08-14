import os

series = {}
notas = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

qnt = int(input("Digite a quantidade de séries que você assistiu nas férias:"))

for i in range(qnt):
    os.system('cls')
    serie = input(f"Digite o nome da {i+1}ª série:")
    nota = input(f"Digite uma nota de 0-10 que você daria para a {i+1}ª série:")
    posicao = input(f'Digite a posição da série {i+1}:')
    lista = [nota, posicao]
    if nota not in notas:
        voltar = input("Você digitou uma nota fora da escala permitida, aperte qualquer botão para encerrar o programa:")
        if voltar != '':
            exit()
    else:
        series.update({serie: lista})

while True:
    os.system('cls')
    adc = input('Digite a nova série para adicionar:')
    nota = input(f"Digite uma nota de 0-10 que você daria para {adc}:")
    posicao = input(f'Digite a posição da série {adc}:')
    lista = [nota, posicao]
    if nota not in notas:
        voltar = input("Você digitou uma nota fora da escala permitida, aperte qualquer botão para encerrar o programa:")
        if voltar != '':
            exit()
    else:
        series.update({adc: lista})
        break

while True:
    os.system('cls')
    print(series)
    pos = input('Digite a série que deseja descobrir a posição:')
    if pos in series:
        print(f'Posição: {series[pos][1]}')
    else:
        voltar = input("A série não está na lista, aperte qualquer botão para encerrar o programa:")
        if voltar != '':
            exit()
    break

while True:
    print(series)
    remover = input('Digite a série que deseja remover:')
    if remover in series:
        series.pop(remover)
    else:
        voltar = input("A série não está na lista, aperte qualquer botão para encerrar o programa:")
        if voltar != '':
            exit()
    break

print(series)
