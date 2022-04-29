from ast import match_case
from listedData import *
from prettytable import PrettyTable # python -m pip install -U prettytable
# from main import header, mainMenu

"""
    searchPlayer: nome do jogador (string) -> string
    Se o jogador for encontrado, a string será formada por: nome do jogador, clube do jogador, todos os status do jogador.
    Se o jogador não for encontrado: 'Jogador não encontrado.'
"""
def searchPlayer(nomeJogador):
    pass

"""
    searchTeam: nome do clube (string) -> lista ou string
    Se o clube for encontrado, retornará uma lista formada pelas ocorrências de clube nos dados, junto com seus jogadores e respectivos status.
    Se o clube não for encontrado: 'Clube não encontrado.'
"""
def searchTeam(nomeClube):
    pass

"""
    searchByPosition: posicao -> lista
    A lista possuirá todas as ocorrências de jogadores com a posição desejada.
"""
def searchByPosition(posicao):
    pass

"""
    searchStatusByRange -> status, início do intervalo, fim do intervalo -> lista ou string
    Se encontrar jogadores com os valores desejados, retorna uma lista contendo todos esses jogadores, com seus respectivos status e nomes de clube.
    Se não encontrar nenhum jogador com status dentro do intervalo: 'Nenhum jogador foi encontrado com status_placeholder possuindo valor entre início_placeholder e fim_placeholder'
    
    status (int): 1 - Overall | 2 - Pace | 3 - Shooting | 4 - Passing | 5 - Dribbling | 6 - Defending | 7 - Physical
"""
def searchStatusByRange(status, inicioIntervalo, fimIntervalo):
    match status:
        case 1:
            statusData = overall[:]
        case 2:
            statusData = pace[:]
        case 3:
            statusData = shooting[:]
        case 4:
            statusData = passing[:]
        case 5:
            statusData = dribbling[:]
        case 6:
            statusData = defending[:]
        case 7:
            statusData = physical[:]

    originalIndexes = insertionSort(statusData)
    
    validValue = False

    while True:
        ans = binarySearch(statusData, 0, len(statusData) - 1, inicioIntervalo)

        if ans != -1:
            validValue = True
            break
        
        inicioIntervalo += 1

        if inicioIntervalo >= fimIntervalo:
            break
    
    if validValue:
        table = PrettyTable(['PLAYER', 'CLUB', 'POSITION', 'OVERALL', 'PACE', 'SHOOTING', 'PASSING', 'DRIBBLING', 'DEFENDING', 'PHYSICAL'])
        for i in range(ans, len(statusData)):
            if statusData[i] > fimIntervalo:
                break
            index = originalIndexes[i]
            table.add_row([playerNames[index], clubs[index], position[index], overall[index], pace[index], shooting[index], passing[index], dribbling[index], defending[index], physical[index]])

        print(table)

        opcao = 0
        while opcao != 1:
            opcao = int(input('\n\nDigite 1 para continuar: '))
    
    else:
        opcao = 0
        while opcao != 1:
            print('\nNenhum jogador encontrado com o status desejado dentro do intervalo informado.')
            opcao = int(input('\n\nDigite 1 para continuar: '))
        
"""
    groupTeams -> _ -> lista
    A lista possuirá todos os dados, agrupando as informações considerando o nome do clube.
    ** O agrupamento ocorrerá considerando as primeiras ocorrências de cada nome. 
    ** Todo: implementar agrupamentos por ordem crescente / decrescente alfabética.
"""
def groupTeams():
    pass

"""
    groupPositions -> _ -> lista
    A lista possuirá todos os dados, agrupando as informações considerando o nome da posição.
    ** O agrupamento ocorrerá considerando as primeiras ocorrências de cada nome. 
    ** Todo: implementar agrupamentos por ordem crescente / decrescente alfabética.
"""
def groupPositions():
    pass

"""
    sortPlayerNames -> ordem -> lista
    A lista conterá todos os dados, apresentando-os a partir de ordenamento sobre os nomes dos jogadores. 'ordem' indica se o ordenamento será crescente
    ou decrescente.

    ordem(int): 1 - Crescente | 2 - Decrescente
"""
def sortPlayerNames(ordem):
    pass

"""
    sortTeamNames -> ordem -> lista
    A lista conterá todos os dados, apresentando-os a partir de ordenamento sobre os nomes dos clubes. 'ordem' indica se o ordenamento será crescente
    ou decrescente.

    ordem(int): 1 - Crescente | 2 - Decrescente
"""
def sortTeamNames(ordem):
    pass

"""
    sortPlayerStatus -> status, ordem -> lista
    A lista conterá todos os dados, apresentando-os a partir de ordenamento sobre os status dos jogadores. 'ordem' indica se o ordenamento será crescente
    ou decrescente.

    status (int): 1 - Overall | 2 - Pace | 3 - Shooting | 4 - Passing | 5 - Dribbling | 6 - Defending | 7 - Physical
    ordem(int): 1 - Crescente | 2 - Decrescente
"""
def sortPlayerStatus(status, ordem):
    pass

"""
    Faz o ordenamento de arr inplace, retornando um array que relaciona os elementos ordenados aos seus índices originais
"""
def insertionSort(arr):
    indexes = [0]
    
    for j in range(1, len(arr)):
        indexes.append(j)
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            indexes[i+1] = indexes[i]
            i -= 1
        arr[i+1] = key
        indexes[i+1] = j

    return indexes

def binarySearch(statusData, left, right, value):
    if right >= left:
 
        middle = (right + left) // 2
 
        if statusData[middle] == value:
            return middle

        elif statusData[middle] > value:
            return binarySearch(statusData, left, middle - 1, value)

        else:
            return binarySearch(statusData, middle + 1, right, value)
 
    else:
        return -1