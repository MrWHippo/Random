
def insertion_sort(array):
    NotSorted = True
    index = 1

    while NotSorted == True:
        storeindex = index
        for x in range(index):
            if array[index] < array[index-1]:
                array[index], array[index - 1] = array[index - 1], array[index]
                index -= 1
            else:
                break
        index = storeindex + 1
        if index == len(array):
            NotSorted = False
    return array