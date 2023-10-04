import math
from random import randint

def f(x):
    if x%10 == 9:
        return x**2
    elif x%10 == 3:
        return x-1
    else:
        return math.factorial(x)

def is_factorial(x):
    print("called")
    running = True
    i = 1
    while running:
        if x == 1:
            return True
        if x%i == 0:
            x //= i
            i += 1
        else:
            return False

def odd(x):
    return (x%2 == 1)

values = [1,2,3,6,8,10,11,12,14]
some_nums = []


n = int(input("Enter number of numbers: "))
u = int(input("Enter upper bound: "))
for x in range(n):
    some_nums.append(randint(0,u))

print(some_nums)


messing_around = True
if messing_around == False:
    # map(f,values) is the same as [f(x) for x in values]
    print(list(map(f,values)))
    print([f(x) for x in values])
    print("------")
    print([n for n in values if odd(n)])
    print([n+4 for n in values if n%2 == 1])
    # filter(odd,values) is the same as [n for n in values if odd(n)]
    print(list(filter(odd,values)))

else:
    print([n for n in some_nums if is_factorial])
    print(list(filter(is_factorial, some_nums)))