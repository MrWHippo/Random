
L1 = ['Stii','rk','ill','Nop','giu']

def remove_dup(string):
    string = list(string)
    newstr = []
    newstr.append(string[0])
    for x in range(1,len(string)):
        IN = False
        for l in newstr:
            if string[x] == l:
                IN = True
        if IN == False:
            newstr.append(string[x])
        else:
            IN = False
        
    return "".join(newstr)

print(list(map(remove_dup,list(map(lambda x: x.upper(),L1)))))