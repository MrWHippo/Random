from random import randint

# function to find the number of passes
def calc(num, num_pass):

    digits = list(str(num))

    value = 1
    for i in digits:
        value *= int(i)
    num_pass += 1

    print(value)
    if len(list(str(value))) == 1:
        print(f"Passes: {num_pass}")
        return "Finished"
    
    calc(value, num_pass)

# 277777788888899
calc(27777777777888888888899, 0)

# pick a 'good' number
def num_picker():
    snum = randint(2,4)
    


