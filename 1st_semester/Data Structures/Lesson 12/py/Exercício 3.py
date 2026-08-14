# Listas com modelos de veículos e os anos correspondentes
modelos_veiculos = ["Fiat Palio", "Ford Fiesta", "Chevrolet Onix", "Volkswagen Gol"]
anos_veiculos = [2021, 2020, 2018, 2023]

# Mostrar os dados dos veículos
print("Veículo\t\tAno")
print("-" * 30)
for modelo, ano in zip(modelos_veiculos, anos_veiculos):
    print(f"{modelo}\t\t{ano}")
print("-" * 30)

# Encontrar o veículo com o maior ano
veiculo_maior_ano = modelos_veiculos[anos_veiculos.index(max(anos_veiculos))]
maior_ano = max(anos_veiculos)

# Encontrar o veículo com o menor ano
veiculo_menor_ano = modelos_veiculos[anos_veiculos.index(min(anos_veiculos))]
menor_ano = min(anos_veiculos)

# Mostrar o veículo com maior ano
print(f"Veículo com maior ano: {veiculo_maior_ano} - Ano: {maior_ano}")

# Mostrar o veículo com menor ano
print(f"Veículo com menor ano: {veiculo_menor_ano} - Ano: {menor_ano}")

# Mostrar o primeiro veículo cadastrado
primeiro_veiculo = modelos_veiculos[0]

# Mostrar o último veículo cadastrado
ultimo_veiculo = modelos_veiculos[-1]

# Mostrar a quantidade de veículos cadastrados
quantidade_veiculos = len(modelos_veiculos)

print(f"Primeiro veículo cadastrado: {primeiro_veiculo}")
print(f"Último veículo cadastrado: {ultimo_veiculo}")
print(f"Quantidade de veículos cadastrados: {quantidade_veiculos}")
