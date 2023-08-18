def chop(t):
    del t[0]
    del t[-1]

def middle(t):
    new = t[1:]
    del new[-1]
    return new 

ls = [5,6,7,8]

#print(chop(ls))

print(middle(ls))
