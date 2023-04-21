
Array = []

Sum = input("Enter Reverse Polish Notation(, inbetween each number/operation): ")
Sum = Sum.split(",")
print(Sum)
for x in range(len(Sum)):
    try:
        Array.append(int(Sum[x]))
    except:
        if Sum[x] == "x" or Sum[x] == "X" or Sum[x] == "*":
            answer = Array[-2] * Array[-1]
            Array.remove(Array[-2])
            Array.remove(Array[-1])
            Array.append(answer)
            
        elif Sum[x] == "/":
            answer = Array[-2] / Array[-1]
            Array.remove(Array[-2])
            Array.remove(Array[-1])
            Array.append(answer)
            
        elif Sum[x] == "-":
            answer = Array[-2] - Array[-1]
            Array.remove(Array[-2])
            Array.remove(Array[-1])
            Array.append(answer)
            
        elif Sum[x] == "+":
            answer = Array[-2] + Array[-1]
            Array.remove(Array[-2])
            Array.remove(Array[-1])
            Array.append(answer)
        else:
            print(f"Error,{Sum[x]} is an invalid input.")

        
print("Answer: ",Array[0])