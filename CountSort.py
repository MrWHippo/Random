
inputarray = [88,73,44,1,8,19,31,63,74,54,19,3,7]
num = 89
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