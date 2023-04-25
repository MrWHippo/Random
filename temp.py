from BubbleSortM import bubble_sort
from InsertionSortM import insertion_sort
import time
from random import randint

array = []
lenarray = int(input("Enter length of array: "))
for x in range(lenarray):
    array.append(randint(0,1000))

array2 = array
print("Bubble")
bubTimeIn = time.time()
bubble_sort(array)
bubTimeFi = time.time()
bubTimeDiff = bubTimeFi - bubTimeIn
print("Bubble Sort Time: ",bubTimeDiff)
print("Insertion")
inTimeIn = time.time()
insertion_sort(array2)
inTimeFi = time.time()
inTimeDiff = inTimeFi - inTimeIn
print("Insertion Sort Time: ",inTimeDiff)
