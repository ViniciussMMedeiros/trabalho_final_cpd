# from ast import match_case
# from listedData import *
import pickle
from prettytable import PrettyTable # python -m pip install -U prettytable
from listedData import Trie
# from main import header, mainMenu

"""
    searchPlayer: nome do jogador (string) -> string
    Se o jogador for encontrado, a string será formada por: nome do jogador, clube do jogador, todos os status do jogador.
    Se o jogador não for encontrado: 'Jogador não encontrado.'
"""
def searchPlayer(nomeJogador):
    result = triePlayerNames.search(nomeJogador)

    # print(playerNames[index])

    if result:
        index = int(result)
    
        table = PrettyTable(['PLAYER', 'CLUB', 'POSITION', 'OVERALL', 'PACE', 'SHOOTING', 'PASSING', 'DRIBBLING', 'DEFENDING', 'PHYSICAL'])

        table.add_row([playerNames[index], clubs[index], position[index], overall[index], pace[index], shooting[index], passing[index], dribbling[index], defending[index], physical[index]])
        
        print(table)
    else:
        print('Jogador não encontrado!')

    opcao = 0

    while(opcao != 1):
        opcao = int(input('\nDigite 1 para voltar: '))

"""
    searchTeam: nome do clube (string) -> lista ou string
    Se o clube for encontrado, retornará uma lista formada pelas ocorrências de clube nos dados, junto com seus jogadores e respectivos status.
    Se o clube não for encontrado: 'Clube não encontrado.'
"""
def searchTeam(nomeClube):
    dictIndexesValues(clubs)

    table = PrettyTable(['PLAYER', 'CLUB', 'POSITION', 'OVERALL', 'PACE', 'SHOOTING', 'PASSING', 'DRIBBLING', 'DEFENDING', 'PHYSICAL'])

    if dictIndexes.get(nomeClube):
        for i in range(len(dictIndexes[nomeClube])):
            index = dictIndexes[nomeClube][i]
            table.add_row([playerNames[index], clubs[index], position[index], overall[index], pace[index], shooting[index], passing[index], dribbling[index], defending[index], physical[index]])

        print(table)
    else:
        print('Clube não encontrado!')

    opcao = 0

    while(opcao != 1):
        opcao = int(input('\nDigite 1 para voltar: '))

"""
    searchByPosition: posicao -> lista
    A lista possuirá todas as ocorrências de jogadores com a posição desejada.
"""
def searchByPosition(posicaoNum):
    dictIndexesValues(position)
    posList = ['RB', 'ST', 'CB', 'GK', 'CM', 'CDM', 'LB', 'RM', 'RW', 'LM', 'SS', 'CAM', 'LWB', 'RWB', 'LW']

    posicao = posList[posicaoNum - 1]

    table = PrettyTable(['PLAYER', 'CLUB', 'POSITION', 'OVERALL', 'PACE', 'SHOOTING', 'PASSING', 'DRIBBLING', 'DEFENDING', 'PHYSICAL'])

    for i in range(len(dictIndexes[posicao])):
        index = dictIndexes[posicao][i]
        table.add_row([playerNames[index], clubs[index], position[index], overall[index], pace[index], shooting[index], passing[index], dribbling[index], defending[index], physical[index]])

    print(table)

    opcao = 0

    while(opcao != 1):
        opcao = int(input('\nDigite 1 para voltar: '))
"""
    searchStatusByRange -> status, início do intervalo, fim do intervalo -> lista ou string
    Se encontrar jogadores com os valores desejados, retorna uma lista contendo todos esses jogadores, com seus respectivos status e nomes de clube.
    Se não encontrar nenhum jogador com status dentro do intervalo: 'Nenhum jogador foi encontrado com status_placeholder possuindo valor entre início_placeholder e fim_placeholder'
    
    status (int): 1 - Overall | 2 - Pace | 3 - Shooting | 4 - Passing | 5 - Dribbling | 6 - Defending | 7 - Physical
"""
def searchStatusByRange(status, inicioIntervalo, fimIntervalo):
    # Copia os valores (não apenas umas referência) para a variável statusData todo o conteúdo do respectivo status selecionado pelo usuário 
    # (faz isso para o ordenamento não afetar a lista original)
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

    originalIndexes = insertionSort(statusData)         # Ordena os dados do status escolhido, neste momento statusData estará ordenado e os índices originais correspondentes estarão em originalIndexes    
    # Exemplo:
    # Lista original -> [4, 3, 2, 1], seus índices são claramente [0, 1, 2, 3]
    # Após ordenamento -> [1, 2, 3, 4], originalIndexes guardará os valores originais dos índices -> [3, 2, 1, 0]. Assim sabe-se que o valor 1 encontrava-se no índice 3 dos dados originais, por exemplo.
    
    validValue = False  # Variável de controle para indicar quando a busca binária abaixo encontrou um valor ou não (-1)

    while True:
        # Faz a busca binária sobre o statusData (lembrando: já está ordenado), com o limite da esquerda sendo 0, o da direita o fim da lista e o valor procurando sendo o inicio do intervalo
        # Ou seja, faz uma busca binária para indicar (se existir) onde está o valor de inicio do intervalo indicado pelo usuário
        ans = binarySearch(statusData, 0, len(statusData) - 1, inicioIntervalo)

        if ans != -1:   # Se não for -1, então a busca binária conseguiu encontrar o valor na lista
            validValue = True   # Atualiza a flag
            break   # Sai do laço (while true)
        
        inicioIntervalo += 1    # Caso não tenha conseguido encontrar o valor (tenha sido -1), então soma 1 ao valor do início do intervalo.
        # Exemplo:
        # O usuário quer o valor 26 como início do intervalo, mas esse valor não existe dentro do status especificado, então nós vamos incrementando até encontrar um valor que existe
        # Sempre considerando que esse valor não pode ultrapassar o fim do intervalo que o usuário quer (condicional abaixo)
        # Ex: início 26, fim 32
        # Faz busca binária procurando por 26, 27, 28, 29, 30, 31 --> Se encontrar qualquer um desses, guarda a sua posição, se não encontrar então não há correspondências para os valores desejados

        if inicioIntervalo >= fimIntervalo:
            break
    
    # Aqui estamos fora do laço, se caiu aqui ou encontrou o valor válido e deu break, ou não encontrou e deu break porque o valor de início do intervalo bateu no valor de fim do intervalo
    if validValue:
        # Cria uma 'PrettyTable' com todas as colunas do csv original para servir como header (colunas) da tabela
        table = PrettyTable(['PLAYER', 'CLUB', 'POSITION', 'OVERALL', 'PACE', 'SHOOTING', 'PASSING', 'DRIBBLING', 'DEFENDING', 'PHYSICAL'])
        # Então, o laço abaixo percorrerá os índices do statusData ordenado anteriormente. 
    
        for i in range(ans, len(statusData)):
            # Funcionamento: Parte do índice encontrado para o início do intervalo no laço while true acima. Então, para cada um desses índices, procura no originalIndexes o índice
            # real correspondente ao dado ordenado dentro do ordenamento original do csv.
            if statusData[i] > fimIntervalo:
                break   # Para apenas quando chegar ao fim do intervalo de valores que o usuário desejava
            index = originalIndexes[i]
            # Cria uma linha na tabela contendo os dados (em ordem, correspondendo aos dados usados para as colunas acima). Observar que os dados são acessados usando 'index', ou seja, o índice original dentro da lista correspondente ao CSV.
            table.add_row([playerNames[index], clubs[index], position[index], overall[index], pace[index], shooting[index], passing[index], dribbling[index], defending[index], physical[index]])

        # Por fim, imprime o resultado da busca para o usuário, usando a table (PrettyTable) criada no laço acima
        print(table)

        # Mantém a tela (o resultado obtido), enquanto o usuário interagir para continuar.
        opcao = 0
        while opcao != 1:
            opcao = int(input('\n\nDigite 1 para continuar: '))
    
    # Caso contrário, a busca binária não conseguiu encontrar um início de intervalo válido nos dados, logo a busca do usuário não retornou resultados válidos.
    # Mantém essa tela de interação para deixar claro para o usuário que a sua busca foi inválida, aguarda por interação.
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
    createArrayValuesIndexes(clubs)
    sortedClubs = radixSortMSBValuesIndexes(arrValuesIndexes, 0)
    
    table = PrettyTable(['PLAYER', 'CLUB', 'POSITION', 'OVERALL', 'PACE', 'SHOOTING', 'PASSING', 'DRIBBLING', 'DEFENDING', 'PHYSICAL'])

    for i in range(len(sortedClubs)):
        index = sortedClubs[i][1]
        table.add_row([playerNames[index], clubs[index], position[index], overall[index], pace[index], shooting[index], passing[index], dribbling[index], defending[index], physical[index]])

    print(table)   

    opcao = 0

    while(opcao != 1):
        opcao = int(input('\nDigite 1 para voltar: '))

"""
    groupPositions -> _ -> lista
    A lista possuirá todos os dados, agrupando as informações considerando o nome da posição.
    ** O agrupamento ocorrerá considerando as primeiras ocorrências de cada nome. 
    ** Todo: implementar agrupamentos por ordem crescente / decrescente alfabética.
"""
def groupPositions():
    dictIndexesValues(position)
    opcao = 0
    
    posList = ['RB', 'ST', 'CB', 'GK', 'CM', 'CDM', 'LB', 'RM', 'RW', 'LM', 'SS', 'CAM', 'LWB', 'RWB', 'LW']

    table = PrettyTable(['I', 'PLAYER', 'CLUB', 'POSITION', 'OVERALL', 'PACE', 'SHOOTING', 'PASSING', 'DRIBBLING', 'DEFENDING', 'PHYSICAL'])

    ind = 1
    for posicao in posList:
        for i in range(len(dictIndexes[posicao])):
            index = dictIndexes[posicao][i]
            table.add_row([ind, playerNames[index], clubs[index], position[index], overall[index], pace[index], shooting[index], passing[index], dribbling[index], defending[index], physical[index]])
            # print(table)
            ind += 1
    print(table)

    while(opcao != 1):
        opcao = int(input('\nDigite 1 para voltar: '))

"""
    sortPlayerNames -> ordem -> lista
    A lista conterá todos os dados, apresentando-os a partir de ordenamento sobre os nomes dos jogadores. 'ordem' indica se o ordenamento será crescente
    ou decrescente.

    ordem(int): 1 - Crescente | 2 - Decrescente
"""
def sortPlayerNames(ordem):
    createArrayValuesIndexes(playerNames)

    sortedNames = radixSortMSBValuesIndexes(arrValuesIndexes, 0)
    
    if ordem == 2:
        descendingFromAscendingOrdered(sortedNames)
        sortedNames = descendingArr

    table = PrettyTable(['PLAYER', 'CLUB', 'POSITION', 'OVERALL', 'PACE', 'SHOOTING', 'PASSING', 'DRIBBLING', 'DEFENDING', 'PHYSICAL'])

    for i in range(len(sortedNames)):
        index = sortedNames[i][1]
        table.add_row([playerNames[index], clubs[index], position[index], overall[index], pace[index], shooting[index], passing[index], dribbling[index], defending[index], physical[index]])

    print(table)   

    opcao = 0

    while(opcao != 1):
        opcao = int(input('\nDigite 1 para voltar: '))

"""
    sortTeamNames -> ordem -> lista
    A lista conterá todos os dados, apresentando-os a partir de ordenamento sobre os nomes dos clubes. 'ordem' indica se o ordenamento será crescente
    ou decrescente.

    ordem(int): 1 - Crescente | 2 - Decrescente
"""
def sortTeamNames(ordem):
    createArrayValuesIndexes(clubs)

    sortedClubs = radixSortMSBValuesIndexes(arrValuesIndexes, 0)
    
    if ordem == 2:
        descendingFromAscendingOrdered(sortedClubs)
        sortedClubs = descendingArr        

    table = PrettyTable(['PLAYER', 'CLUB', 'POSITION', 'OVERALL', 'PACE', 'SHOOTING', 'PASSING', 'DRIBBLING', 'DEFENDING', 'PHYSICAL'])


    # sum = 0
    for i in range(len(sortedClubs)):
        index = sortedClubs[i][1]
        table.add_row([playerNames[index], clubs[index], position[index], overall[index], pace[index], shooting[index], passing[index], dribbling[index], defending[index], physical[index]])
        # sum += 1

    print(table)   
    # print(sum)

    opcao = 0

    while(opcao != 1):
        opcao = int(input('\nDigite 1 para voltar: '))

"""
    sortPlayerStatus -> status, ordem -> lista
    A lista conterá todos os dados, apresentando-os a partir de ordenamento sobre os status dos jogadores. 'ordem' indica se o ordenamento será crescente
    ou decrescente.

    status (int): 1 - Overall | 2 - Pace | 3 - Shooting | 4 - Passing | 5 - Dribbling | 6 - Defending | 7 - Physical
    ordem(int): 1 - Crescente | 2 - Decrescente
"""
def sortPlayerStatus(status, ordem):
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

    originalIndexes = insertionSort(statusData)         # Ordena os dados do status escolhido, neste momento statusData estará ordenado e os índices originais correspondentes estarão em originalIndexes   
    
    if ordem == 2:
        descendingFromAscendingOrdered(originalIndexes)
        originalIndexes = descendingArr

    table = PrettyTable(['PLAYER', 'CLUB', 'POSITION', 'OVERALL', 'PACE', 'SHOOTING', 'PASSING', 'DRIBBLING', 'DEFENDING', 'PHYSICAL'])

    for i in range(len(statusData)):
        index = originalIndexes[i]
        table.add_row([playerNames[index], clubs[index], position[index], overall[index], pace[index], shooting[index], passing[index], dribbling[index], defending[index], physical[index]])

    print(table)

    opcao = 0

    while(opcao != 1):
        opcao = int(input('\nDigite 1 para voltar: '))

def addPlayer(playerNameValue, clubName, positionName, overallValue, paceValue, shootingValue, passingValue, dribblingValue, defendingValue, physicalValue):
    nameAdd = playerNameValue + '@' + str(len(playerNames))

    playerNames.append(playerNameValue)
    clubs.append(clubName)
    position.append(positionName)
    overall.append(overallValue)
    shooting.append(shootingValue)
    pace.append(paceValue)
    passing.append(passingValue)
    dribbling.append(dribblingValue)
    defending.append(defendingValue)
    physical.append(physicalValue)

    # print(len(playerName))

    triePlayerNames.add(nameAdd)

    updatePkl()
    loadPkl()

    print(playerNames)

    opcao = 0

    while(opcao != 1):
        opcao = int(input('\nDigite 1 para voltar: '))

def removePlayer():
    pass

"""
    Faz o ordenamento de arr localmente, retornando uma lista que relaciona os elementos ordenados aos seus índices originais
    Exemplo de funcionamento: [] -> key |||| * --> ponteiro esquerda (i)
    
    Arr			        Indices originais
    [1, 5, 4, 3, 2]		[0]
    [1, [5], 4, 3, 2]	[0, 1]
    [1*, [5], 4, 3, 2]	[0, 1]
    [1, 5*, [4], 3, 2]	[0, 1, 2]
    [1, 5, 5, 3, 2]		[0, 1, 1]		-> Key = 4
    [1*, 5, 5, 3, 2]	[0, 1, 1]		-> Key = 4
    [1, 4, 5, 3, 2]		[0, 2, 1]
    [1, 4, 5*, [3], 2]	[0, 2, 1, 3]
    [1, 4*, 5, 5, 2]	[0, 2, 1, 1]		-> Key = 3
    [1, 4, 4, 5, 2]		[0, 2, 2, 1]		-> Key = 3
    [1, 3, 4, 5, 2]		[0, 3, 2, 1]
    [1, 3, 4, 5*, [2]]	[0, 3, 2, 1, 4]
    [1, 3, 4, 5*, 5]	[0, 3, 2, 1, 1]		-> Key = 2
    [1, 3, 4*, 5, 5]	[0, 3, 2, 1, 1]		-> Key = 2
    [1, 3, 4*, 4, 5]	[0, 3, 2, 2, 1]		-> Key = 2
    [1, 3*, 4, 4, 5]	[0, 3, 2, 2, 1]		-> Key = 2
    [1, 3*, 3, 4, 5]	[0, 3, 3, 2, 1]		-> Key = 2
    [1*, 3, 3, 4, 5]	[0, 3, 3, 2, 1]		-> Key = 2
    [1, 2, 3, 4, 5]		[0, 4, 3, 2, 1]
    Dados ordenados ->		    [1, 2, 3, 4, 5]
    Seus índices originais ->	[0, 4, 3, 2, 1]
"""
def insertionSort(arr):
    originalIndexes = [0]   # array para guardar os índices originais dos dados ordenados
    
    for index in range(1, len(arr)):    # percorre todos os índices dentro do array, começando por 1
        originalIndexes.append(index)           # salva o índice atual no array de índices originais
        key = arr[index]                        # Faz a lógica do insertion sort, mantem o elemento atual como a key
        i = index - 1                           # Cria um ponteiro 'i' auxiliar para ir percorrendo para a esquerda a partir da key
        
        while i >= 0 and arr[i] > key:          # Enquanto o ponteiro não tiver chegado no início dos dados, e o valor para o qual aponta for maior do que a key, continua
            arr[i+1] = arr[i]                   # Copia o valor da esquerda para a direita
            originalIndexes[i+1] = originalIndexes[i] # No array de índices originais, copia o valor do índice da esquerda para a direita
            i -= 1                              # Decrementa o ponteiro da esquerda
        
        # quando sair do laço (ponteiro menor que o limite da esquerda ou valor da key menor que o valor encontrado), coloca de volta a key para a posição a direita do ponteiro
        arr[i+1] = key
        # faz a mesma coisa para o valor do índice
        originalIndexes[i+1] = index

    return originalIndexes

# Busca binária tradicional (feita de forma recursiva), usando uma variável (statusData) que guarda um dos status dos jogadores de forma ordenada, limites de 
# esquerda e direita (que por padrão são chamados como 0 e o len - 1 da lista) e o valor a ser procurado.
# Se encontar o valor, retorna seu índice. Se não encontrar, retorna -1.
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
 
def dictIndexesValues(arr):
    global dictIndexes
    dictIndexes = {}

    for i in range(len(arr)):
        pos = arr[i]
        if not (pos in dictIndexes):
            dictIndexes[pos] = [i]
            continue
        dictIndexes[pos].append(i)

def createArrayValuesIndexes(arr): # [['value': index], ['value2', index2]]
    global arrValuesIndexes
    arrValuesIndexes = [None] * len(arr)

    for i in range(len(arr)):
        arrValuesIndexes[i] = [arr[i], i]

def radixSortMSBValuesIndexes(array, i):
    if len(array) <= 1:
        return array

    done_bucket = []
    buckets = [ [] for x in range(0,381) ]

    for el in array:
        if i >= len(el[0]):
            done_bucket.append(el)
        else:   
            buckets[ ord(el[0][i]) - ord('a') ].append(el)

    buckets = [ radixSortMSBValuesIndexes (b, i + 1) for b in buckets ]

    return done_bucket + [ b for blist in buckets for b in blist ]

def descendingFromAscendingOrdered(arr):
    global descendingArr

    descendingArr = []

    for i in range(len(arr) - 1, -1, -1):
        descendingArr.append(arr[i]) 

def loadPkl():
    global triePlayerNames, playerNames, clubs, position, overall, pace, shooting, passing, dribbling, defending, physical
    triePlayerNames = Trie()

    with open('./src/dataFiles/triePlayerNames.pkl', 'rb') as f:
        triePlayerNames = pickle.load(f)
    with open('./src/dataFiles/playerNames.pkl', 'rb') as f:
        playerNames = pickle.load(f)
    with open('./src/dataFiles/clubs.pkl', 'rb') as f:
        clubs = pickle.load(f)
    with open('./src/dataFiles/position.pkl', 'rb') as f:
        position = pickle.load(f)
    with open('./src/dataFiles/overall.pkl', 'rb') as f:
        overall = pickle.load(f)
    with open('./src/dataFiles/pace.pkl', 'rb') as f:
        pace = pickle.load(f)
    with open('./src/dataFiles/shooting.pkl', 'rb') as f:
        shooting = pickle.load(f)
    with open('./src/dataFiles/passing.pkl', 'rb') as f:
        passing = pickle.load(f)
    with open('./src/dataFiles/dribbling.pkl', 'rb') as f:
        dribbling = pickle.load(f)
    with open('./src/dataFiles/defending.pkl', 'rb') as f:
        defending = pickle.load(f)
    with open('./src/dataFiles/physical.pkl', 'rb') as f:
        physical = pickle.load(f)

loadPkl()

def updatePkl():
    with open('./src/dataFiles/triePlayerNames.pkl', 'wb') as f:
        pickle.dump(triePlayerNames, f)
    with open('./src/dataFiles/playerNames.pkl', 'wb') as f:
        pickle.dump(playerNames, f)
    with open('./src/dataFiles/clubs.pkl', 'wb') as f:
        pickle.dump(clubs, f)
    with open('./src/dataFiles/position.pkl', 'wb') as f:
        pickle.dump(position, f)
    with open('./src/dataFiles/overall.pkl', 'wb') as f:
        pickle.dump(overall, f)
    with open('./src/dataFiles/pace.pkl', 'wb') as f:
        pickle.dump(pace, f)
    with open('./src/dataFiles/shooting.pkl', 'wb') as f:
        pickle.dump(shooting, f)
    with open('./src/dataFiles/passing.pkl', 'wb') as f:
        pickle.dump(passing, f)
    with open('./src/dataFiles/dribbling.pkl', 'wb') as f:
        pickle.dump(dribbling, f)
    with open('./src/dataFiles/defending.pkl', 'wb') as f:
        pickle.dump(defending, f)
    with open('./src/dataFiles/physical.pkl', 'wb') as f:
        pickle.dump(physical, f)
