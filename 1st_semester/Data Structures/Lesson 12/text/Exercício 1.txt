# Lista de nomes dos clientes
nomes_clientes = ["João", "Maria", "Pedro", "Ana"]

# Lista de saldos das contas em reais
saldos_contas = [1350.00, 3240.00, 2100.50, 5000.75]

# Mostrar os dados dos clientes
print("Nome Cliente\tSaldo Conta R$")
print("-" * 30)
for nome, saldo in zip(nomes_clientes, saldos_contas):
    print(f"{nome}\t\t{saldo:.2f}")
print("-" * 30)

# Encontrar o cliente com o maior saldo
cliente_maior_saldo = nomes_clientes[saldos_contas.index(max(saldos_contas))]
maior_saldo = max(saldos_contas)

# Encontrar o cliente com o menor saldo
cliente_menor_saldo = nomes_clientes[saldos_contas.index(min(saldos_contas))]
menor_saldo = min(saldos_contas)

# Mostrar o cliente com maior saldo
print(f"Cliente com maior saldo: {cliente_maior_saldo} - Saldo: {maior_saldo:.2f}")

# Mostrar o cliente com menor saldo
print(f"Cliente com menor saldo: {cliente_menor_saldo} - Saldo: {menor_saldo:.2f}")
