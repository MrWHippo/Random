
#def next(n):
#    return 3*n +1

# lambda replaces ^^^^
num = 3
if num == 1:
    next = lambda n: 3*n+1
    # means: take n and return 3n +1

    plus = lambda x,y: x+y

    print(plus(2,3))

    L = [3,6,8]
    print(list(map(next,L)))

    print(list(filter(lambda x: x%2 == 0, L)))

elif num ==2:
    square = lambda x: x**2
    list_to_be_squared = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    print(list(filter(lambda x: x%3 ==0, list(map(square,list_to_be_squared)))))

else:
    plus =lambda x,y: x+y
    # partial application of plus
    f = lambda n: plus(n,5)
