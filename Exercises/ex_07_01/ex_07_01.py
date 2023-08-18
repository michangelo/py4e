fh = open('mbox-short.txt')
# print(fh)

for lx in fh:
    ly = lx.rstrip() # use `rstrip()` to remove \n at end of line
    print(ly.upper()) # use `upper()` to shout file 