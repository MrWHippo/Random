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
            if array_empty == False:
                if int(values) < array[-1]:
                    [print("Invalid num, each number has to be bigger than the last.")]
                else:
                    array.append(int(values))
            else:
                array.append(int(values))
                array_empty = False
        
Accept = False
while Accept == False:
    value = (input("Enter Search Value: "))
    try:
        value = int(value)
        Accept = True
    except:
        pass

def binary_search(value, array, start_index, end_index):
    if start_index >= end_index:
        return None
    mid_index = (start_index + end_index) //2
    if array[mid_index] == value:
        return mid_index
    else:
        if array[mid_index] > value:
            return binary_search(value, array, start_index, mid_index)
        elif array[mid_index] < value:
            return binary_search(value, array, mid_index+1 , end_index)
        else:
            print("Error")
            return None

print(array)
print(binary_search(value, array, 0, len(array)-1))




