from random import randint
inputarray = []

lenarray = int(input("Enter length of array: "))
for x in range(lenarray):
    inputarray.append(randint(1,1000))

#inputarray = [5,4,3,2,1]

num = 1001
tally = [0]*num

for value in inputarray:
    tally[value] += 1

for i in range(1, len(tally)):
    tally[i] += tally[i-1]

result = [0]*(tally[-1])

for value in inputarray:
    result[tally[value-1]] = value
    tally[value-1] += 1

print(result)