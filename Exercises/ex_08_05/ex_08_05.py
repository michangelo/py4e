def exercise_8_5():

    """
    1. Open the file mbox-short.txt and read it line by line. 
    2. When you find a line that starts with 'From ' like the following line:
        `From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008`
    3. Parse the From line using split()
    4. Print out the second word in the line (entire address of person who sent msg)
    5. Print the count at the end
    Hint: Make sure not to include the lines that start with "From:".
          Look at last line of sample output to see how to print the count:
          `There were 27 lines in the file with From as the first word`
    """

    # fname = input("Enter file name: ")
    # fhandle = open(fname)

    fhandle = open("mbox-short.txt")        # Open file mbox-short.txt
    count = 0                               # initialize count to 0 
    words = list()
    for line in fhandle:                    # iterate each line in fhandle
        count = count + 1 
        line = line.rstrip()                # strip whitespace 
        # print("Line:", line)
        # Guardian to skip blank lines
        # if line == "":
            # print("Skip Blank")
            # continue
        words = line.split()                # split words 
        # print("Debug:", words)
        # Guardian a bit stronger
        # if len(words) < 3:
            # continue
        

        # Guardian in a compound statement 
        if len(words) < 3 or words[0] != "From":
            # print("Ignore")
            continue
        print(words[2])
    print("There were", count, "lines in the file with From as the first word")
exercise_8_5()