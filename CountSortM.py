
## num = biggest in array

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