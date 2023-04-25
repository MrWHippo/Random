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

initialtime = time.time()

for Pass in range(len(array)):
    swapped = False
    for index in range(1,len(array)-Pass):
        if array[index] < array[index - 1]:
            swapped = True
            array[index], array[index - 1] = array[index - 1], array[index]
    if swapped == False:
        break

finaltime = time.time()
timediff = finaltime-initialtime

print(array)
print(timediff)