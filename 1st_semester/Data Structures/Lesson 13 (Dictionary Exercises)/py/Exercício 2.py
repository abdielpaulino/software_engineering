estados = {
    "Acre": "Capital Rio Branco",
    "Alagoas": "Capital Maceió",
    "Amazonas": "Capital Manaus",
    "Bahia": "Capital Salvador",
    "Distrito Federal": "Capital Brasília",
    "Santa Catarina": "Capital Florianópolis",
    "Rio Grande do Sul": "Capital Porto Alegre",
    "Paraná": "Capital Curitiba",
    "São Paulo": "Capital São Paulo",
    "Minas Gerais": "Cuiabá",
    "Rio de Janeiro": "Rio de Janeiro",
    "Tocantins": "Capital Palmas"
}

print (estados)

novo_estado = input("Digite o nome do novo estado: ")
nova_capital = input(f"Digite a capital de {novo_estado}: ")
estados[novo_estado] = nova_capital

posicao_df = list(estados.keys()).index("Distrito Federal") + 1
print(f"A posição do Distrito Federal é: {posicao_df}")

nova_capital_mg = input("Digite a nova capital de Minas Gerais: ")
estados["Minas Gerais"] = nova_capital_mg

print("\nLista completa de estados e capitais:")
for estado, capital in estados.items():
    print(f"{estado}: {capital}")