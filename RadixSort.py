from CountSortM import count_sort_radix
from GetBiggestM import get_biggest

def radix_sort(array):
    stillgoing = False
    x = 100
    while stillgoing == False:
        stillgoing = False
        for num in range(len(array)):
            if array[num] < x:
                array[num] = 0
            else:
                stillgoing = True
        array = count_sort_radix(array, (x+1))
        x *= 10
    return array


array = [88,73,44,1,8,19,31,63,74,54,19,3,7]



def radix_sort_2(array):
    largestval = get_biggest(array)
    print(largestval)
    x = 10
    for num in range(int(len(str(largestval)))-1):
        print("Hi")
        for i in range(len(array)):
            if array[i] < x:
                array[i] = 0
        array = count_sort_radix(array, x)
        
    return array




print(radix_sort_2(array))
