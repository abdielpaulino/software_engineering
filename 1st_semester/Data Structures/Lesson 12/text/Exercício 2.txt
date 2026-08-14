# Listas com nomes de frutas, quantidade em estoque e preço do quilo
frutas = ["Laranja", "Banana", "Maçã", "Uva"]
estoque = [35, 20, 40, 15]
preco_quilo = [4.25, 3.75, 2.50, 6.00]

# Mostrar os dados das frutas
print("Fruta\t\tQtde Estoque\t\tPreço Kg")
print("-" * 40)
for fruta, qtd, preco in zip(frutas, estoque, preco_quilo):
    print(f"{fruta}\t\t{qtd}\t\t\t{preco:.2f}")
print("-" * 40)

# Encontrar a fruta com a maior quantidade em estoque
fruta_maior_estoque = frutas[estoque.index(max(estoque))]
maior_estoque = max(estoque)

# Encontrar a fruta com a menor quantidade em estoque
fruta_menor_estoque = frutas[estoque.index(min(estoque))]
menor_estoque = min(estoque)

# Mostrar a fruta com maior quantidade em estoque
print(f"Fruta com maior quantidade em estoque: {fruta_maior_estoque} - Qtde: {maior_estoque}")

# Mostrar a fruta com menor quantidade em estoque
print(f"Fruta com menor quantidade em estoque: {fruta_menor_estoque} - Qtde: {menor_estoque}")

# Calcular e mostrar a soma total das quantidades de frutas em estoque
soma_total = sum(estoque)
print(f"Soma total das quantidades em estoque: {soma_total}")
