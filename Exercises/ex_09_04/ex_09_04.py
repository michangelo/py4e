# fname = input('Enter file name: ')
# fhand = open(fname)
# c = dict()
# for line in fhand:
#     if not line.startswith('From '): continue
#     pieces = line.split()
#     email = pieces[1]
#     c[email] = c.get(email, 0) + 1

# print(c)

import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)