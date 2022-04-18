from listedData import *

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
    pass

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