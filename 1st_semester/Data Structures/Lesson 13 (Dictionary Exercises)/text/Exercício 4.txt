import os

# Criando o dicionário de atletas famosos
atletas = {
    "Cristiano Ronaldo": "Futebol",
    "LeBron James": "Basquete",
    "Lionel Messi": "Futebol",
    "Neymar": "Futebol",
    "Conor McGregor": "MMA",
    "Roger Federer": "Tênis",
    "Rafael Nadal": "Tênis",
    "Stephen Curry": "Basquete",
    "Tiger Woods": "Golfe",
    "Kevin Durant": "Basquete",
    "Lewis Hamilton": "Fórmula 1",
    "Sun Yang": "Natação"
}

print("\nLista completa de atletas:")
for posicao, (atleta, esporte) in enumerate(atletas.items(), start=1):
    print(f"{posicao}: {atleta} - {esporte}")

novo_atleta = input("Digite o nome do novo atleta: ")
novo_esporte = input(f"Digite o esporte de {novo_atleta}: ")
atletas.update({novo_atleta: novo_esporte})

posicao_federer = list(atletas.keys()).index("Roger Federer") + 1
print(f"A posição do Roger Federer é: {posicao_federer}")

del atletas["Tiger Woods"]

print("\nLista completa de atletas:")
for posicao, (atleta, esporte) in enumerate(atletas.items(), start=1):
    print(f"{posicao}: {atleta} - {esporte}")
