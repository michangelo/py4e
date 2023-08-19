#fname = input("Enter file name: ")
#fhandle = open(fname)

fhandle = open('mbox-short.txt')
count = 0
for line in fhandle:
    count = count + 1 
    line = line.rstrip()
    #print("Line:", line)

    # Guardian to skip blank lines
    #if line == "":
    #     print("Skip Blank")
    #     continue
    words = line.split()
    #print('Debug:', words)
    # Guardian a bit stronger
    # if len(words) < 3:
    #      continue

    # Guardian in a compound statement
    if len(words) < 3 or words[0] != "From":
        # print("Ignore")
        continue 
    print(words[2]) 
print(count)
# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     # print('Debug:', words)
#     if len(words) == 0 or words[0] != 'From' : continue
#     print(words[2])