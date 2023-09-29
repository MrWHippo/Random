from functools import reduce

# normal way
values = [2,3,6,4,1,2]

def add(current_total, num):
    return current_total + num

def mult(current_total, num):
    return current_total * num

def HCF(num1,num2):
    



current_total = values[0]
for item in values[1:]:
    current_total = add(current_total, item)
print(current_total)

# or 

print(reduce(add, values))
print(reduce(mult, values))