#fname = input("Enter file name: ")
#fhandle = open(fname)

fhandle = open('mbox-short.txt')

for line in fhandle:
    line = line.rstrip()
    print("Line:", line)
    words = line.split()
    print('Debug:', words)
    if len(words) < 1:
        continue
    if words[0] != "From":
        print("Ignore")
        continue 
    print(words[2])

# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     # print('Debug:', words)
#     if len(words) == 0 or words[0] != 'From' : continue
#     print(words[2])