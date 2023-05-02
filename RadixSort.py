from CountSortM import count_sort


def radix_sort(array):
    stillgoing = False
    x = 10
    while stillgoing == False:
        stillgoing = False
        for num in range(len(array)):
            if array[num] < x:
                array[num] = 0
            else:
                stillgoing = True
                array[num] = array[num]%x
        array = count_sort(array, x)
        x *= 10
    return array


array = [88,73,44,1,8,19,31,63,74,54,19,3,7]

radix_sort(array)

