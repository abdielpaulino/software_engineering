class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivo(no.direita, valor)

    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no, valor):
        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self._remover_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover_recursivo(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            no.valor = self._min_valor(no.direita)
            no.direita = self._remover_recursivo(no.direita, no.valor)

        return no

    def _min_valor(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no.valor

    def pesquisar(self, valor):
        print("Elementos na árvore:")
        self._mostrar_recursivo(self.raiz)
        return self._pesquisar_recursivo(self.raiz, valor)

    def _pesquisar_recursivo(self, no, valor):
        if no is None or no.valor == valor:
            return no
        if valor < no.valor:
            return self._pesquisar_recursivo(no.esquerda, valor)
        return self._pesquisar_recursivo(no.direita, valor)

    def _mostrar_recursivo(self, no):
        if no is not None:
            self._mostrar_recursivo(no.esquerda)
            print(no.valor, end=" ")
            self._mostrar_recursivo(no.direita)

# Função para interação com o usuário
def menu():
    arvore = ArvoreBinaria()
    elementos = [43, 11, 62, 9, 41, 48, 95]
    for elemento in elementos:
        arvore.inserir(elemento)

    while True:
        print("\nMenu:")
        print("1. Incluir novo nó")
        print("2. Excluir nó")
        print("3. Pesquisar nó e mostrar árvore")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            valor = int(input("Digite o valor do novo nó: "))
            arvore.inserir(valor)
        elif escolha == '2':
            valor = int(input("Digite o valor do nó a ser removido: "))
            if arvore.pesquisar(valor):
                arvore.remover(valor)
                print("Nó removido com sucesso!")
            else:
                print("Nó não encontrado na árvore.")
        elif escolha == '3':
            valor = int(input("Digite o valor do nó a ser pesquisado: "))
            if arvore.pesquisar(valor):
                print("\nNó encontrado na árvore.")
            else:
                print("\nNó não encontrado na árvore.")
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
