# Solicita ao usuário que insira a idade das pessoas
idades = []

while True:
    idade = input("Digite as idades das pessoas (digite 'fim' para encerrar):")
    if idade.lower() == 'fim':
        break
    else:
        idades.append(int(idade))

# Ordena a lista de idades
idades.sort()

# Mostra a lista de idades na ordem menor para maior
print("Lista de idades na ordem menor para maior:")
print(idades)
