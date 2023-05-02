
## num = biggest in array +1

def count_sort(inputarray, num):
    tally = [0]*num

    for value in inputarray:
        tally[value] += 1

    for i in range(1, len(tally)):
        tally[i] += tally[i-1]

    result = [0]*(tally[-1])

    for value in inputarray:
        result[tally[value-1]] = value
        tally[value-1] += 1

    return result
### works as long as array doesnt contain any 0s ^^^^^^

def test_count_sort(inputarray, max):
    tally = [0]*(max)

    for value in inputarray:
        tally[value] += 1
    
    for i in range(1,len(tally)):
        tally[i] += tally[i-1]

    result = [None]*(tally[-1]+1)

    for value in inputarray:
        result[tally[value-1]] = value
        tally[value-1] += 1
    
    return result

array = [88,73,44,1,8,0,19,31,63,74,54,19,3,7]

#print(count_sort(array, 89))
print(test_count_sort(array, 89))
