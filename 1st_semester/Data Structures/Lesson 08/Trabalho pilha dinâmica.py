from collections import deque

expressao = input("Digite sua expressão: ")
x=True
pilha = deque()
for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        if not pilha:
            print ("A expressão não está balanceada.")
            x=False
            break
        else:
            pilha.pop()

if len(pilha) == 0 and x==True:
    print ("A expressão está balanceada.")