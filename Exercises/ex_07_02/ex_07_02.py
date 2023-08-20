def exercise_7_2():
    # Use the file name mbox-short.txt as the file name
    fname = input("Enter file name: ")
    # first, be pythonic with error message
    try:
        fh = open(fname) 
    except: 
        print('File cannot be opened:', fname)
        exit()
    # next, set counters and iterate through for loop 
    count = 0
    spam = 0.0 
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        count = count + 1
        spam = spam + float(line[-7:]) #.rstrip()) # float `line` and remove whitespace
        avg_spam = spam/count      
    print('Average spam confidence:', avg_spam)
exercise_7_2()

