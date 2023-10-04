
def only_odd(n):
    return (n%2 == 1)

L = [1,2,3,4,5,6]

print(list(filter(only_odd,L)))