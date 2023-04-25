import time

array = []
arraytext = ""
while len(arraytext) == 0:
    arraytext = input("Enter array: ")
arraytext = arraytext.split(",")
for x in range(len(arraytext)):
    try:
        array.append(int(arraytext[x]))
    except:
        print("Only numbers will be placed in array.")

NotSorted = True
index = 1

initialtime = time.time()
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

finaltime = time.time()
timediff = finaltime - initialtime

print(array)
print("Time taken: ",timediff)