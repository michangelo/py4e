def ex_9_4():
    done = False 
    while not done:
        try:
            name = input("Enter file: ")
            if len(name) < 1:
                name = "mbox-short.txt"
            handle = open(name)
            done = True
        except:
            print("File does not exist")

    histogram = dict()

    for line in handle:
        line_split = line.split()
        if len(line_split) > 0 and line_split [0] == "From":
            # print(line_split)
            email = line_split[1]
            histogram[email] = histogram.get(email, 0) + 1

    maxCount = max(histogram.values())

    for email in histogram:
        if histogram[email] == maxCount:
            print(email, maxCount)
            return 

ex_9_4()
