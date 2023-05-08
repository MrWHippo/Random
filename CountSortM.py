
## num = biggest in array + 1

def count_sort(inputarray, num):
    tally = [0]*num
    for i in range(len(inputarray)):
        inputarray[i] += 1

    for value in inputarray:
        tally[value] += 1

    for i in range(1, len(tally)):
        tally[i] += tally[i-1]

    result = [0]*(tally[-1])

    for value in inputarray:
        result[tally[value-1]] = value
        tally[value-1] += 1
    
    for i in range(len(result)):
        result[i] -= 1

    return result

## num = %

def count_sort_radix(inputarray, num):
    x = num + 1
    tally = [0]*x
    for i in range(len(inputarray)):
        inputarray[i] += 1

    for value in inputarray:
        tally[value%num] += 1

    for i in range(1, len(tally)):
        tally[i] += tally[i-1]

    result = [0]*(tally[-1])

    for value in inputarray:
        result[tally[value%num]] = value
        tally[(value%num)] += 1
    
    for i in range(len(result)):
        result[i] -= 1

    return result



array = [88,73,44,1,8,19,31,63,74,54,19,3,7]
print(count_sort_radix(array, 10))


