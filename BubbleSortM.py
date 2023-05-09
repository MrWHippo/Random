
def bubble_sort(array):
    for Pass in range(len(array)):
        swapped = False
        for index in range(1,len(array)-Pass):
            if array[index] < array[index - 1]:
                swapped = True
                array[index], array[index - 1] = array[index - 1], array[index]
        if swapped == False:
            break
    return array


def bubble_sort_2D(array):
    for Pass in range(len(array)):
        swapped = False
        for index in range(1,len(array)-Pass):
            if array[index][0] < array[index - 1][0]:
                swapped = True
                array[index], array[index - 1] = array[index - 1], array[index]
        if swapped == False:
            break
    return array