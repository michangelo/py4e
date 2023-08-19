def exercise_9_4():
    """
    1. Write a program to read through the mbox-short.txt and
    figure out who has sent the greatest number of mail messages. 
    2. The program looks for 'From ' lines and takes the second word of 
    those lines as the person who sent the mail. 
    3. The program creates a Python dictionary that maps the sender's mail 
    address to a count of the number of times they appear in the file. 
    After the dictionary is produced, the program reads through the dictionary 
    using a maximum loop to find the most prolific committer.
    """
    fname = input('Enter file name: ')                                      # enter mbox-short.txt
    fhandle = open(fname)                                                   # open file and store as file handle
    my_dictionary = dict()                                                  # initialize empty dictionary
    try:                                                                    # be pythonic with errors 
        fhandle = open(fname)                                   
    except:
        print("Invalid file name:", fname)
        exit()                                                              # and gracefully exit
    for line in fhandle:                                                    # iterate through each line in fhandle
        if not line.startswith('From '): continue                           # skip if line starts with From
        words = line.split()                                                # separate words in list                  
        email_word = words[1]                                               # get the email only
        # idiom: retrieve/create/update counter
        my_dictionary[email_word] = my_dictionary.get(email_word, 0) + 1    # if the key is not there, the count is 0
    
    bigc = None                                                             # now, find most common  
    bige = None
    for word in my_dictionary:
        value = my_dictionary[word]
        if bigc is None or value > bigc:
            bigw = word
            bigc = value
    print(bigw, bigc)
    
exercise_9_4()