fname = input("Enter file name: ")
fhandle = open(fname)

for line in fhandle:
    line = line.rstrip()
    words = line.split()
    print('Debug:', words)
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