import pickle
from trieData import Trie

# with open('./src/dataFiles/playerNames.pkl', 'rb') as f:
#     playerNames = pickle.load(f)

# with open('./src/dataFiles/playerNames.pkl', 'rb') as f:
#     try:
#         while True:
#             # triePlayerNames = pickle.load(f)
#             playerNames = pickle.load(f)
#             print('\n\n\n\n\n')
#             print(playerNames)
#     except EOFError:
#             pass

arr = [1, 2, 3, 4, 5]

del arr[1]

print(arr)

# triePlayerNames = Trie()

# with open('./src/dataFiles/triePlayerNames.pkl', 'rb') as f:
#     triePlayerNames = pickle.load(f)

# print(playerNames)


# print(triePlayerNames.search('Joao'))