#IMPORTAÇÕES
import os #Limpar tela

#CRIANDO LISTAS
lista_filmes = []
lista_series = []
opcoes_do_menu = [1, 2, 0]

#CRIANDO MENU

while True:

    #MENU
    print ("\n")
    print ("-" * 34)
    print ("  MINHA LISTA DE FILMES E SERIES  ")
    print ("-" * 34)

    print ("\nAbrir lista de filmes: 1")
    print ("Abrir lista de series: 2")
    print ("Encerrar programa: 0")

    #ESCOLHENDO OPÇÃO DE LISTA
    escolha_menu = input("\nEscolha o valor de acordo com a opção desejada: ")

    match escolha_menu:

        #ENCERRAR PROGRAMA
        case '0':
            break
     
        #MODIFICAR LISTA DE FILMES
        case '1':
            os.system('cls')
            print ("\nESCOLHA OQUE VOCÊ DESEJA MUDAR NA SUA LISTA DE FILMES:")
            print ("\nInserir filme: 1")
            print ("Pesquisar filme: 2")
            print ("Excluir filme: 3")
            print ("Imprimir lista de filmes: 4")
            print ("Encerrar programa: 0")

            escolha_modificação_lista_filme = input("\nEscolha o valor de acordo com a opção desejada: ")

            #OQUE MUDAR NA LISTA DE FILMES
            match escolha_modificação_lista_filme:

                #INSERIR
                case '1':
                    os.system('cls')
                    print ("\nInserir ao final da lista: 1")
                    print ("Inserir em uma posição específica: 2")
                    print ("Encerrar programa: 0")

                    escolha_como_inserir = input("\nEscolha o valor de acordo com a opção desejada: ")

                    if escolha_como_inserir == '1':
                        os.system('cls')
                        filme_fim_da_lista = input("\nDigite o nome do filme que deseja inserir ao final da lista: ")
                        lista_filmes.append(filme_fim_da_lista)
                        
                    elif escolha_como_inserir == '2':
                        os.system('cls')
                        posicao_da_lista = int(input("\nDigite a posição que deseja inserir o filme na lista: "))
                        filme_que_ira_na_posicao = input("\nDigite o filme que irá na posição escolhida anteriormente: ")
                        lista_filmes.insert(posicao_da_lista, filme_que_ira_na_posicao);
                        if posicao_da_lista > len(lista_filmes):
                            posicao_invalida = input("\nEstá posição é inválida no momento, presione qualquer caractere para encerrar o programa: ")
                            if posicao_invalida != all:
                                break
                            
                    elif escolha_como_inserir == '0':
                        break

                    else:
                        os.system('cls')
                        print("\nO VALOR DIGITADO NÃO FOI ENCONTRADO NAS OPÇÕES ACIMA!")
                        valor_nao_encontrado = input("\nDIGITE QUALQUER CARACTERE PARA ENCERRAR O PROGRAMA: ")

                        if valor_nao_encontrado != all:
                            break

                #PESQUISAR
                case '2':
                    os.system('cls')
                    print ("\nPesquisar pelo nome: 1")
                    print ("Pesquisar pela posição: 2")
                    print ("Encerrar programa: 0")

                    escolha_como_pesquisar = input("\nEscolha o valor de acordo com a opção desejada: ")

                    if escolha_como_pesquisar == '1':
                        os.system('cls')
                        pesquisar_filme_pelo_nome = input("\nDigite o nome do filme que deseja pesquisar na lista: ")
                        if pesquisar_filme_pelo_nome in lista_filmes:
                            print ("\nO filme procurado está na lista.")
                        else:
                            filme_nao_encontrado = input("\nO filme procurado não esta na lista, presione qualquer caractere para encerrar o programa: ")
                            if filme_nao_encontrado != all:
                                break

                    elif escolha_como_pesquisar == '2':
                        os.system('cls')
                        pesquisar_filme_pela_posicao = int(input("\nDigite a posição que deseja pesquisar na lista: "))
                        if  0 <= pesquisar_filme_pela_posicao < len(lista_filmes):
                            print ("\nO filme que está na posição", pesquisar_filme_pela_posicao, "é",  lista_filmes[pesquisar_filme_pela_posicao])

                        else:
                            posicao_invalida = input("\nEstá posição é inválida no momento, presione qualquer caractere para encerrar o programa: ")
                            if posicao_invalida != all:
                                break
                        
                    elif escolha_como_pesquisar == '0':
                        break

                    else:
                        os.system('cls')
                        print("\nO VALOR DIGITADO NÃO FOI ENCONTRADO NAS OPÇÕES ACIMA!")
                        valor_nao_encontrado = input("\nDIGITE QUALQUER CARACTERE PARA ENCERRAR O PROGRAMA: ")

                        if valor_nao_encontrado != all:
                            break

                #EXCLUIR
                case '3':
                    os.system('cls')
                    print ("\nExcluir pelo nome: 1")
                    print ("Excluir pela posição: 2")
                    print ("Encerrar programa: 0")

                    escolha_como_excluir = input("\nEscolha o valor de acordo com a opção desejada: ")

                    if escolha_como_excluir == '1':
                        os.system('cls')
                        excluir_filme_pelo_nome = input("\nDigite o nome do filme que deseja excluir da lista: ")
                        if excluir_filme_pelo_nome in lista_filmes:
                            lista_filmes.remove(excluir_filme_pelo_nome)
                            print ("\nO filme foi removido da lista.")
                        else:
                            filme_nao_encontrado = input("\nO filme procurado não esta na lista, presione qualquer caractere para encerrar o programa: ")
                            if filme_nao_encontrado != all:
                                break

                    elif escolha_como_excluir == '2':
                        os.system('cls')
                        excluir_filme_pela_posicao = int(input("\nDigite a posição que deseja pesquisar na lista: "))
                        if  0 <= excluir_filme_pela_posicao < len(lista_filmes):
                            lista_filmes.pop(excluir_filme_pela_posicao)
                            print ("\nO filme foi removido da lista.")

                        else:
                            posicao_invalida = input("\nEstá posição é inválida no momento, presione qualquer caractere para encerrar o programa: ")
                            if posicao_invalida != all:
                                break
                        
                    elif escolha_como_excluir == '0':
                        break

                    else:
                        os.system('cls')
                        print("\nO VALOR DIGITADO NÃO FOI ENCONTRADO NAS OPÇÕES ACIMA!")
                        valor_nao_encontrado = input("\nDIGITE QUALQUER CARACTERE PARA ENCERRAR O PROGRAMA: ")

                        if valor_nao_encontrado != all:
                            break
                        
                #IMPRIMIR
                case '4':
                    os.system('cls')
                    print ("\nSua lista de filmes até o momento é: ", lista_filmes)

                #ENCERRAR PROGRAMA
                case '0':
                    break

                #OPÇÃO NÃO ENCONTRADA
                case _:
                    os.system('cls')
                    print("\nO VALOR DIGITADO NÃO FOI ENCONTRADO NAS OPÇÕES ACIMA!")
                    valor_nao_encontrado = input("\nDIGITE QUALQUER CARACTERE PARA ENCERRAR O PROGRAMA: ")

                    if valor_nao_encontrado != all:
                            break




        #MODIFICAR LISTA DE SERIES
        case '2':
            os.system('cls')
            print ("\nESCOLHA OQUE VOCÊ DESEJA MUDAR NA SUA LISTA DE SERIES:")
            print ("\nInserir serie: 1")
            print ("Pesquisar serie: 2")
            print ("Excluir serie: 3")
            print ("Imprimir lista de serie: 4")
            print ("Encerrar programa: 0")

            escolha_modificação_lista_serie = input("\nEscolha o valor de acordo com a opção desejada: ")

            #OQUE MUDAR NA LISTA DE SERIES
            match escolha_modificação_lista_serie:

                #INSERIR
                case '1':
                    os.system('cls')
                    print ("\nInserir ao final da lista: 1")
                    print ("Inserir em uma posição específica: 2")
                    print ("Encerrar programa: 0")

                    escolha_como_inserir = input("\nEscolha o valor de acordo com a opção desejada: ")

                    if escolha_como_inserir == '1':
                        os.system('cls')
                        serie_fim_da_lista = input("\nDigite o nome da serie que deseja inserir ao final da lista: ")
                        lista_series.append(serie_fim_da_lista)
                        
                    elif escolha_como_inserir == '2':
                        os.system('cls')
                        posicao_da_lista = int(input("\nDigite a posição que deseja inserira serie na lista: "))
                        serie_que_ira_na_posicao = input("\nDigite a serie que irá na posição escolhida anteriormente: ")
                        lista_series.insert(posicao_da_lista, serie_que_ira_na_posicao);
                        if posicao_da_lista > len(lista_series):
                            posicao_invalida = input("\nEstá posição é inválida no momento, presione qualquer caractere para encerrar o programa: ")
                            if posicao_invalida != all:
                                break
                            
                    elif escolha_como_inserir == '0':
                        break

                    else:
                        os.system('cls')
                        print("\nO VALOR DIGITADO NÃO FOI ENCONTRADO NAS OPÇÕES ACIMA!")
                        valor_nao_encontrado = input("\nDIGITE QUALQUER CARACTERE PARA ENCERRAR O PROGRAMA: ")

                        if valor_nao_encontrado != all:
                            break

                #PESQUISAR
                case '2':
                    os.system('cls')
                    print ("\nPesquisar pelo nome: 1")
                    print ("Pesquisar pela posição: 2")
                    print ("Encerrar programa: 0")

                    escolha_como_pesquisar = input("\nEscolha o valor de acordo com a opção desejada: ")

                    if escolha_como_pesquisar == '1':
                        os.system('cls')
                        pesquisar_serie_pelo_nome = input("\nDigite o nome da serie que deseja pesquisar na lista: ")
                        if pesquisar_serie_pelo_nome in lista_series:
                            print ("\nO filme procurado está na lista.")
                        else:
                            serie_nao_encontrado = input("\nA serie procurado não esta na lista, presione qualquer caractere para encerrar o programa: ")
                            if serie_nao_encontrado != all:
                                break

                    elif escolha_como_pesquisar == '2':
                        os.system('cls')
                        pesquisar_serie_pela_posicao = int(input("\nDigite a posição que deseja pesquisar na lista: "))
                        if  0 <= pesquisar_serie_pela_posicao < len(lista_series):
                            print ("\nA serie que está na posição", pesquisar_serie_pela_posicao, "é",  lista_series[pesquisar_serie_pela_posicao])

                        else:
                            posicao_invalida = input("\nEstá posição é inválida no momento, presione qualquer caractere para encerrar o programa: ")
                            if posicao_invalida != all:
                                break
                        
                    elif escolha_como_pesquisar == '0':
                        break

                    else:
                        os.system('cls')
                        print("\nO VALOR DIGITADO NÃO FOI ENCONTRADO NAS OPÇÕES ACIMA!")
                        valor_nao_encontrado = input("\nDIGITE QUALQUER CARACTERE PARA ENCERRAR O PROGRAMA: ")

                        if valor_nao_encontrado != all:
                            break

                #EXCLUIR
                case '3':
                    os.system('cls')
                    print ("\nExcluir pelo nome: 1")
                    print ("Excluir pela posição: 2")
                    print ("Encerrar programa: 0")

                    escolha_como_excluir = input("\nEscolha o valor de acordo com a opção desejada: ")

                    if escolha_como_excluir == '1':
                        os.system('cls')
                        excluir_serie_pelo_nome = input("\nDigite o nome da serie que deseja excluir da lista: ")
                        if excluir_serie_pelo_nome in lista_series:
                            lista_series.remove(excluir_serie_pelo_nome)
                            print ("\nA serie foi removido da lista.")
                        else:
                            serie_nao_encontrado = input("\nA serie procurado não esta na lista, presione qualquer caractere para encerrar o programa: ")
                            if serie_nao_encontrado != all:
                                break

                    elif escolha_como_excluir == '2':
                        os.system('cls')
                        excluir_serie_pela_posicao = int(input("\nDigite a posição que deseja pesquisar na lista: "))
                        if  0 <= excluir_serie_pela_posicao < len(lista_series):
                            lista_series.pop(excluir_serie_pela_posicao)
                            print ("\nA serie foi removido da lista.")

                        else:
                            posicao_invalida = input("\nEstá posição é inválida no momento, presione qualquer caractere para encerrar o programa: ")
                            if posicao_invalida != all:
                                break
                        
                    elif escolha_como_excluir == '0':
                        break

                    else:
                        os.system('cls')
                        print("\nO VALOR DIGITADO NÃO FOI ENCONTRADO NAS OPÇÕES ACIMA!")
                        valor_nao_encontrado = input("\nDIGITE QUALQUER CARACTERE PARA ENCERRAR O PROGRAMA: ")

                        if valor_nao_encontrado != all:
                            break
                        
                #IMPRIMIR
                case '4':
                    os.system('cls')
                    print ("\nSua lista de series até o momento é: ", lista_series)

                #ENCERRAR PROGRAMA
                case '0':
                    break

                #OPÇÃO NÃO ENCONTRADA
                case _:
                    os.system('cls')
                    print("\nO VALOR DIGITADO NÃO FOI ENCONTRADO NAS OPÇÕES ACIMA!")
                    valor_nao_encontrado = input("\nDIGITE QUALQUER CARACTERE PARA ENCERRAR O PROGRAMA: ")

                    if valor_nao_encontrado != all:
                            break
                        
        #POSIÇÃO NÃO ENCONTRADA
        case _:     
            os.system('cls')
            print("\nO VALOR DIGITADO NÃO FOI ENCONTRADO NAS OPÇÕES ACIMA!")
            valor_nao_encontrado = input("\nDIGITE QUALQUER CARACTERE PARA ENCERRAR O PROGRAMA: ")

            if valor_nao_encontrado != all:
                    break
                        
