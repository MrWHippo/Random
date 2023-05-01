from BubbleSortM import bubble_sort
from InsertionSortM import insertion_sort
from MergeSortM import merge_sort
import time
from random import randint

array = []
array2 = []
array3 = []
lenarray = int(input("Enter length of array: "))
for x in range(lenarray):
    array.append(randint(0,1000))
    array2.append(randint(0,1000))
    array3.append(randint(0,1000))

# 3 = all 1 = merge
testchoice = 1
if testchoice == 3:
    print("Bubble Sort:")
    bubTimeIn = time.time()
    bubble_sort(array)
    bubTimeFi = time.time()
    bubTimeDiff = bubTimeFi - bubTimeIn
    print("Bubble Sort Time: ",bubTimeDiff)
    ####
    print("Insertion Sort:")
    inTimeIn = time.time()
    insertion_sort(array2)
    inTimeFi = time.time()
    inTimeDiff = inTimeFi - inTimeIn
    print("Insertion Sort Time: ",inTimeDiff)
####
print("Merge Sort:")
MeTimeIn = time.time()
merge_sort(array3)
MeTimeFi = time.time()
MeTimeDiff = MeTimeFi - MeTimeIn
print("Merge Sort Time: ",MeTimeDiff)

# seconds
#10000 = BS:4 IS:3
#50000 = BS:107 IS:81
#5M = Merge:17