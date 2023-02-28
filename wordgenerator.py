
file = open("WordsGenerated.txt","w")

base1 = 97
base2 = 97
base3 = 97
base4 = 97
base5 = 97
count = 0
done = False
while done == False:
    tempword = chr(base5) + chr(base4) + chr(base3) + chr(base2) + chr(base1) 
    file.write(tempword + "\n")
    count += 1
    if base1 + 1 != 123:
        base1 += 1
    else:
        base1 = 97
        if base2 + 1 != 123:
            base2 += 1
        else:
            base2 = 97
            if base3 + 1 != 123:
                base3 += 1
            else:
                base3 = 97
                if base4 + 1 != 123:
                    base4 += 1
                else:
                    base4 = 97
                    if base5 + 1 != 123:
                        base5 += 1
                    else:
                        done = True

print("Finished")
file.close()
            
        