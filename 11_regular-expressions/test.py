# search for lines that start with 2 characters, starting with 
import re 
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    expr = '^From:  (.+)'
    if re.search((expr), line):
        print(re.findall(expr, line))