def exercise_8_4():

    """
    1. Open the file romeo.txt and read it line by line.
    2. For each line, split the line into a list of words using the split() method.
    3. The program should build a list of words. 
    4. For each word on each line check to see if the word is already in the list and 
       if not append it to the list.
    5. When the program completes, sort and print the resulting words in python sort()
       order as shown in the desired output.
    """
    
    fname = input("Enter file name: ")         # user input, use romeo.txt
    fhandle = open(fname, "r")                 # open and read file and store as handle
    word_list = list()                         # create empty list for iteration
    for line in fhandle:                       # iterate fhandle line by line  
        words = line.split()                   # split line into list of words
        #print(words)                          # check list of words 
        for word in words:                     # iterate each word in list
            if word in word_list: continue     # if word already exists, continue
            word_list.append(word)             # if not, append the word to empty list
    word_list.sort()                           # sort the final list of words 
    print(word_list)                           # print resulting words 
    
# exercise_8_4()