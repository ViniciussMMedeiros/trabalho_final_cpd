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
            # print(cur)

        if '*' in cur:
            # index = ''.join(cur['@'])
            index = ''.join(cur['*'])
            return index
        else:
            return False

dictionary = Trie()
# nomeJogador + '@' + index -> 'nomeJogador*@112'
# dictionary.add("hi@03")
dictionary.add("hi@1234567")
# dictionary.add("hello")
print(dictionary.search("hi"))
# print(dictionary.search("hello"))
# print(dictionary.search("hel"))
# print(dictionary.search("hey"))