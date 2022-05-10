from listedData import playerNames
import pickle

class Trie:
    head = {}

    def add(self, word):
        flagEscreveuMarcacao = False
        cur = self.head
        for ch in word:
            if flagEscreveuMarcacao:
                cur['*'].append(ch)
                continue
            if ch == '@':
                flagEscreveuMarcacao = True
                cur['*'] = []
                continue
            if ch not in cur:
                cur[ch] = {}

            cur = cur[ch]

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            index = ''.join(cur['*'])
            return index
        else:
            return False

dictTriePlayerNames = Trie()

for i in range(len(playerNames)):
    nameWithIndex = '' + playerNames[i] + '@' + str(i)
    
    dictTriePlayerNames.add(nameWithIndex)

with open('./src/dataFiles/triePlayerNames.pkl', 'wb') as f:
    pickle.dump(dictTriePlayerNames, f)