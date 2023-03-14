while True:
    num = int(input("Enter size of Class: "))
    probnone = 1
    arraysize = 10000 #days in year
    for x in range(num):
        probnone*= (arraysize-x)/arraysize

    probtotal = 1-probnone
    print(probtotal)



