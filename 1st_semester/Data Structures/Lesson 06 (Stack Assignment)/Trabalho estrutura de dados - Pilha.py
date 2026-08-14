class PilhaEstatica:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.pilha = [None] * capacidade

    def vazia(self):
        return self.topo == -1
    
    def cheia(self):
        return self.topo == self.capacidade - 1
    
    def empilhar(self, elemento):
        if self.cheia():
            print("A pilha está cheia. Não é possível adicionar mais elementos.")
            return
        self.topo += 1
        self.pilha[self.topo] = elemento
    
    def desempilhar(self):
        if self.vazia():
            print("A pilha está vazia. Não é possível remover elementos.")
            return None
        elemento = self.pilha[self.topo]
        self.topo -= 1
        return elemento
    
    def mostrar_pilha(self):
        if self.vazia():
            print("A pilha está vazia.")
        else:
            print("Elementos na pilha:")
            for i in range(self.topo + 1):
                print(self.pilha[i])
    
    def tamanho(self):
        return self.topo + 1

# Definindo a capacidade
capacidade = int(input("Digite a capacidade da pilha: "))
pilha = PilhaEstatica(capacidade)

# Menu
while True:
    print("\nMenu:")
    print("1. Adicionar elemento na pilha")
    print("2. Remover elemento da pilha")
    print("3. Mostrar todos os elementos da pilha")
    print("4. Verificar se a pilha está cheia")
    print("5. Verificar se a pilha está vazia")
    print("6. Mostrar tamanho da pilha")
    print("0. Sair")
      
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        elemento = input("Digite o elemento a ser adicionado na pilha: ")
        pilha.empilhar(elemento)

    elif opcao == '2':
        elemento_desempilhado = pilha.desempilhar()
        if elemento_desempilhado is not None:
            print("Elemento removido:", elemento_desempilhado)

    elif opcao == '3':
        pilha.mostrar_pilha()

    elif opcao == '4':
        if pilha.cheia():
            print("A pilha está cheia.")
        else:
            print("A pilha não está cheia.")

    elif opcao == '5':
        if pilha.vazia():
            print("A pilha está vazia.")
        else:
            print("A pilha não está vazia.")

    elif opcao == '6':
        print("Tamanho da pilha:", pilha.tamanho())

    elif opcao == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")
