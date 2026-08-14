# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ").lower()

# Listas
vogais_lista = ['a', 'e', 'i', 'o', 'u']
vogais_na_frase = []
consoantes_na_frase = []
lista_letras = []

# Retirando espaços da frase

frase_sem_espaco = frase.replace(" ", "")

# Analisa cada caractere
for caractere in frase_sem_espaco:
    # Verifica se o caractere é vogal
    if caractere in vogais_lista:
        # Adiciona a letra à lista de vogais
        vogais_na_frase.append(caractere)
        lista_letras.append(caractere)
    else:
        # Se não é vogal adiciona a lista de consoantes
        consoantes_na_frase.append(caractere)
        lista_letras.append(caractere)

print ("Quantidade de vogais:", len(vogais_na_frase))
print ("Quantidade de consoantes", len(consoantes_na_frase))
print ("Todos os caracteres:", lista_letras)

        
