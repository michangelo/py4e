name = input('Enter file: ') # romeo.txt
handle = open(name, 'r')
wordlist = list()
for line in handle:
    words = line.split()
    for word in words:
        if word in wordlist: continue
        wordlist.append(word)

wordlist.sort()
print(wordlist)