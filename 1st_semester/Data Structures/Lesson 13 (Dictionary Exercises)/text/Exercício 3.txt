import os

times = {
    1: "Criciuma",
    2: "Avai",
    3: "Marcilio Dias",
    4: "Joinville",
    5: "Figueirense",
    6: "Chapecoense",
    7: "Brusque",
    8: "Metropolitano",
    9: "Hercílio Luz",
    10: "Inter de Lages"
}

print("\nLista completa de times:")
for posicao, time in times.items():
    print(f"{posicao}: {time}")

novo_time = input("Digite o nome do novo time: ")
times[len(times) + 1] = novo_time


posicao_joinville = list(times.values()).index("Joinville") + 1
print(f"A posição do Joinville é: {posicao_joinville}")


times = {key: value for key, value in times.items() if value != "Avai"}


print("\nLista completa de times:")
for posicao, time in times.items():
    print(f"{posicao}: {time}")
