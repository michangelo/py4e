# class example searching for a word using dictionary vs list 
newword = input('Enter a new word:')
words = open('ourwords.txt').read().split()

# linear search O(n)
print(newword in words)


# Building a Dictionary O(n)
exists = {} 

for word in words:
    exists[word] = True

# "Instant" search using dictionary O(1)
print(exists.get(newword) != None)

# Binary-ish search O(n/2) ~= O(n)
# words.sort()

# middle = len(words)//2

# # we go in the middle
# if words[middle] == newword:
#     print('True')
# # We need to aim higher
# elif words[middle] < newword:
#     for word in words[middle+1:]:
#         print(word == newword)
# # We need to aim lower
# elif words[middle] > newword:
#     for word in words[:middle]:
#         print(word == newword)


