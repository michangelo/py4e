fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# xfile = open('mbox.txt')
# for cheese in xfile:
#     print(cheese)

### Counting Lines in a File 
fhand = open('mbox.txt')
count = 0 
for line in fhand:
    count = count + 1 
print('Line Count:', count)

### Reading the *Whole* File
# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

### Searching Through a File 
# fhand = open('mbox-short.txt')
# for line in fhand:
#     if line.startswith('From:'):
#         print(line)

### Searching Through a File (Fixed)
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

### Skipping with Continue - does same thing as above
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line) 

### Using `in` to select Lines 
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not 'uct.ac.za' in line:
        continue
    print(line)

### Prompt for File Name
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0 
for line in fhand:
    if line.startswith('Subject:'):
        count += 1 
    print('There were', count, 'subject lines in', fname)

### Try and Except for Bad File Names 
# 

