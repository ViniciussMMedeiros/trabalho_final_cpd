import os
import functions
"""
    +   Uma simples função para limpar o terminal e gerar o header do programa.
"""
def header():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
     _________________   _____         _           _ _            ______ _             _           ______ _  __       ___  ____     _____  ______ _                           
    /  __ \ ___ \  _  \ |_   _|       | |         | | |           |  ___(_)           | |          |  ___(_)/ _|      |  \/  | |   /  ___| | ___ \ |                          
    | /  \/ |_/ / | | |   | |_ __ __ _| |__   __ _| | |__   ___   | |_   _ _ __   __ _| |  ______  | |_   _| |_ __ _  | .  . | |   \ `--.  | |_/ / | __ _ _   _  ___ _ __ ___ 
    | |   |  __/| | | |   | | '__/ _` | '_ \ / _` | | '_ \ / _ \  |  _| | | '_ \ / _` | | |______| |  _| | |  _/ _` | | |\/| | |    `--. \ |  __/| |/ _` | | | |/ _ \ '__/ __|
    | \__/\ |   | |/ /    | | | | (_| | |_) | (_| | | | | | (_) | | |   | | | | | (_| | |          | |   | | || (_| | | |  | | |___/\__/ / | |   | | (_| | |_| |  __/ |  \__ \\
     \____|_|   |___/     \_/_|  \__,_|_.__/ \__,_|_|_| |_|\___/  \_|   |_|_| |_|\__,_|_|          \_|   |_|_| \__,_| \_|  |_|_____|____/  \_|   |_|\__,_|\__, |\___|_|  |___/
                                                                                                                                                        __/ |              
                                                                                                                                                        |___/               """)

"""
    +   Uma simples função para encerrar a execução do programa.
"""
def exit():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Programa encerrado')
    raise SystemExit

"""
    +   Função para gerar o menu inicial, responsável por apresentar as principais (todas) as funcionalidades do programa.
"""
def mainMenu():
    opcao = -1

    while(opcao < 1 or opcao > 4):
        header()
        print('\n1 - Pesquisar')
        print('\n2 - Agrupar')
        print('\n3 - Ordenar')
        print('\n4 - Sair')

        opcao = int(input('\nDigite a opção: '))

    match opcao:
        case 1:
            search()
        case 2:
            group()
        case 3:
            sortData()
        case 4:
            exit()

"""
    +   Função para o menu da funcionalidade pesquisar, mostrando as possibilidades de pesquisa que o usuário pode utilizar.
"""
def search():
    opcao = -1

    while(opcao < 1 or opcao > 6):
        header()
        print('\n### Pesquisar ###\n')
        print('\n1 - Jogador')
        print('\n2 - Clube (e apresentar jogadores)')
        print('\n3 - Posição (e apresentar jogadores)')
        print('\n4 - Jogador com status dentro de intervalo')
        print('\n5 - Voltar ao menu')
        print('\n6 - Sair')

        opcao = int(input('\nDigite a opção: '))

    match opcao:
        case 1:
            header()
            nomeJogador = input('Digite o nome do jogador: ')
            functions.searchPlayer(nomeJogador)
        case 2:
            header()
            nomeClube = input('Digite o nome do clube: ')
            functions.searchTeam(nomeClube)
        case 3:
            # opcaoPosicao = -1

            # while(opcaoPosicao < 1 or opcaoPosicao > 9):
            #     header()
            #     print('\n### Pesquisando por status dos jogadores ###\n')
            #     print('\n1 - RB')
            #     print('\n2 - ST')
            #     print('\n3 - CB')
            #     print('\n4 - GK')
            #     print('\n5 - CM')
            #     print('\n6 - CDM')
            #     print('\n7 - LB')
            #     print('\n8 - RM')
            #     print('\n9 - RW')
            #     print('\n10 - LM')
            #     print('\n11 - SS')
            #     print('\n12 - CAM')
            #     print('\n13 - LWB')
            #     print('\n14 - RWB')
            #     print('\n15 - LW')
            #     print('\n8 - Voltar ao menu')
            #     print('\n9 - Sair')

            #     opcaoPosicao = int(input('\nDigite a opção: '))

            # if opcaoPosicao == 8:
            #     mainMenu()
            # elif opcaoPosicao == 9:
            #     exit()

            opcaoPosicao = int(input('\nDigite a posição: '))
            functions.searchByPosition(opcaoPosicao)
        case 4:
            opcaoStatus = -1

            while(opcaoStatus < 1 or opcaoStatus > 9):
                header()
                print('\n### Pesquisando por status dos jogadores ###\n')
                print('\n1 - Overall')
                print('\n2 - Pace')
                print('\n3 - Shooting')
                print('\n4 - Passing')
                print('\n5 - Dribbling')
                print('\n6 - Defending')
                print('\n7 - Physical')
                print('\n8 - Voltar ao menu')
                print('\n9 - Sair')

                opcaoStatus = int(input('\nDigite a opção: '))

            if opcaoStatus == 8:
                mainMenu()
            elif opcaoStatus == 9:
                exit()

            header()
            inicioIntervalo = int(input('\nDigite o início do intervalo: '))
            fimIntervalo = int(input('\nDigite o fim do intervalo: '))
            
            error = True

            if inicioIntervalo >= fimIntervalo:
                print('Erro: O início do intervalo deve ser menor que o fim do intervalo!')
            elif inicioIntervalo < 0:
                print('Erro: O início do intervalo deve ser maior ou igual à 0.')
            elif fimIntervalo > 100:
                print('Erro: O fim do intervalo deve ser menor ou igual à 100.')
            else:
                functions.searchStatusByRange(opcaoStatus, inicioIntervalo, fimIntervalo)
                error = False
            
            if error:
                opcao = 0

                while(opcao != 1):
                    opcao = int(input('\nDigite 1 para voltar: '))
                
                if opcao == 1:
                    search()

            search()
        case 5:
            mainMenu()
        case 6:
            exit()

"""
    +   Função para o menu da funcionalidade agrupar, mostrando as possibilidades de agrupamento de dados que o usuário pode utilizar.
"""
def group():
    opcao = -1

    while(opcao < 1 or opcao > 4):
        header()
        print('\n### Agrupar ###\n')
        print('\n1 - Clubes')
        print('\n2 - Posições')
        print('\n3 - Voltar ao menu')
        print('\n4 - Sair')

        opcao = int(input('\nDigite a opção: '))

    match opcao:
        case 1:
            functions.groupTeams()
        case 2:
            functions.groupPositions()
        case 3:
            mainMenu()
        case 4:
            exit()

"""
    +   Função para o menu da funcionalidade ordenar, mostrando as possibilidades de ordenamento de dados que o usuário pode utilizar.
"""
def sortData():
    opcao = -1

    while(opcao < 1 or opcao > 5):
        header()
        print('\n### Ordenar ###\n')
        print('\n1 - Nomes dos jogadores')
        print('\n2 - Nomes dos clubes')
        print('\n3 - Status dos jogadores')
        print('\n4 - Voltar ao menu')
        print('\n5 - Sair')

        opcao = int(input('\nDigite a opção: '))

    if opcao != 4 and opcao != 5:

        opcaoOrdem = -1

        while(opcaoOrdem < 1 or opcaoOrdem > 2):
            header()
            print('\n### Ordem ###\n')
            print('\n1 - Crescente')
            print('\n2 - Decrescente')

            opcaoOrdem = int(input('\nDigite a opção: '))    

    match opcao:
        case 1:
            functions.sortPlayerNames(opcaoOrdem)
        case 2:
            functions.sortTeamNames(opcaoOrdem)
        case 3:
            opcaoStatus = -1

            while(opcaoStatus < 1 or opcaoStatus > 9):
                header()
                print('\n### Ordenando por status dos jogadores ###\n')
                print('\n1 - Overall')
                print('\n2 - Pace')
                print('\n3 - Shooting')
                print('\n4 - Passing')
                print('\n5 - Dribbling')
                print('\n6 - Defending')
                print('\n7 - Physical')
                print('\n8 - Voltar ao menu')
                print('\n9 - Sair')

                opcaoStatus = int(input('\nDigite a opção: '))

            if opcaoStatus == 8:
                mainMenu()
            elif opcaoStatus == 9:
                exit()

            functions.sortPlayerStatus(opcaoStatus, opcaoOrdem)
        case 4:
            mainMenu()
        case 5:
            exit()

"""
    +   Chamada da função mainMenu para inicializar a interação do usuário com o menu principal.
"""
mainMenu()