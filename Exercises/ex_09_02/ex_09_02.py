# fname = input('Enter file name: ')
# fhand = open(fname)
# c = dict()
# for line in fhand:
#     if not line.startswith('From '): continue
#     pieces = line.split()
#     email = pieces[1]
#     c[email] = c.get(email, 0) + 1

# print(c)

file = open("mbox-short.txt")
days = {}
for line in file:
    line_split = line.split()

    # with guardian 
    if len(line_split) == 0 or line_split[0] != "From":
        continue

    # without guardian ???
    #if len(line_split) > 0 and line_split[0] != "From":

    day = line_split[2]
    days[day] = days.get(day, 0) + 1
print(days)