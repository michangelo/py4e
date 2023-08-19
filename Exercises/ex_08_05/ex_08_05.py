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

    fhandle = open("mbox-short.txt")        # Open file mbox-short.txt
    count = 0                               # initialize count to 0 
    word_list = list()                      # creat empty words_list
    for line in fhandle:                    # iterate each line in fhandle
        line = line.rstrip()                # strip whitespace 
        # print("Line:", line)              # debug: check lines
        # Guardian to skip blank lines      # debug: guardian for blank lines
        # if line == "":
            # print("Skip Blank")
            # continue
        word_list = line.split()            # split word_list 
        # print("Debug:", word_list)        # debug: word_list
        # Guardian a bit stronger           # debug: guardian to skip words < 3
        # if len(word_list) < 3:
            # continue
        # Guardian in a compound statement                  # guardian to keep
        if len(word_list) < 3 or word_list[0] != "From":    # if length less than 3 or doesn't start with from, skip
            # print("Ignore")   
            continue
        count = count + 1                   # set counter here for proper count 
        print(word_list[1])                 # print full address
    print("There were", count, "lines in the file with From as the first word") 
exercise_8_5()
    