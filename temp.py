from BubbleSortM import bubble_sort
from InsertionSortM import insertion_sort
from MergeSortM import merge_sort
from CountSortM import count_sort
import time
from random import randint

array = []
array2 = []
array3 = []
lenarray = int(input("Enter length of array: "))
for x in range(lenarray):
    array.append(randint(1,1000))

array2 = array.copy()
array3 = array.copy()
array4 = array.copy()
    

# 3 = all 1 = merge + count
testchoice = 1
if testchoice == 3:
    bubTimeIn = time.time()
    bubble_sort(array)
    bubTimeFi = time.time()
    bubTimeDiff = bubTimeFi - bubTimeIn
    print("Bubble Sort Time: ",bubTimeDiff)
    ####
    inTimeIn = time.time()
    insertion_sort(array2)
    inTimeFi = time.time()
    inTimeDiff = inTimeFi - inTimeIn
    print("Insertion Sort Time: ",inTimeDiff)

####
MeTimeIn = time.time()
merge_sort(array3)
MeTimeFi = time.time()
MeTimeDiff = MeTimeFi - MeTimeIn
print("Merge Sort Time: ",MeTimeDiff)

####
CoTimeIn = time.time()
count_sort(array4, 1001)
CoTimeFi = time.time()
CoTimeDiff = CoTimeFi - CoTimeIn
print("Count Sort Time: ", CoTimeDiff)

# seconds
#10000 = BS:4 IS:3
#50000 = BS:107 IS:81
#5M = Merge:17