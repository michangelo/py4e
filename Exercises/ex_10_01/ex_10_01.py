
def ex_10_01():
    handle = open(input("Enter file name: "))
    histogram = dict()
    
    for line in handle:
        line_split = line.split()
        if len(line_split) > 0 and line_split [0] == "From":
            # print(line_split)
            email = line_split[1]
            histogram[email] = histogram.get(email, 0) + 1

    reverse_tuples = histogram.items()
    tuples = []

    for email, count in reverse_tuples:
        tuples.append((count, email))

    tuples.sort(reverse=True)
    maxCount, maxEmail = tuples[0]
    print(maxEmail, maxCount)

ex_10_01()

