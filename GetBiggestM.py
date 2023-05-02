
def get_biggest(array):
    currenthigh = 0
    for x in array:
        if x > currenthigh:
            x = currenthigh
    return x

