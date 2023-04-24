array = []
array_empty = True
Exit = False
while Exit == False:
    print("Enter # for end.")
    print("Enter Values for array :")
    values = input()
    if values == "#":
        Exit = True
    else:
        try:
            values = int(values)
            Accepted = True
        except:
            print("Invalid input, Enter a number.")
            Accepted = False
        if Accepted == True:
            array.append(int(values))
        
Accept = False
while Accept == False:
    value = (input("Enter Search Value: "))
    try:
        value = int(value)
        Accept = True
    except:
        pass

def linear_search(value, array):
    for index in range(len(array)):
        if array[index] == value:
            return index
        elif index == len(array):
            return None

print(linear_search(value, array))