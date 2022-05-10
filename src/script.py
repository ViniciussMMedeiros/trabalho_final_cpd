import pickle
from trieData import Trie

with open('./src/dataFiles/playerNames.pkl', 'rb') as f:
    playerNames = pickle.load(f)

# triePlayerNames = Trie()

# with open('./src/dataFiles/triePlayerNames.pkl', 'rb') as f:
#     triePlayerNames = pickle.load(f)

print(playerNames)


# print(triePlayerNames.search('Joao'))