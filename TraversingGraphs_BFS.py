
#undirected graph
class node():
    def __init__(self, selfvalue, neighbour1, neighbour2, neighbour3, neighbour4):
        self.value = selfvalue
        self.neighbour1 = neighbour1
        self.neighbour2 = neighbour2
        self.neighbour3 = neighbour3
        self.neighbour4 = neighbour4

    def get_neighbours(self):
        return self.neighbour1, self.neighbour2, self.neighbour3, self.neighbour4

    def neighbours(self):
        return [self.neighbour1, self.neighbour2, self.neighbour3, self.neighbour4]
    

#####

class LinearQueue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.head = 0
        self.tail = -1
    
    def dequeue(self):
        if self.is_empty() == False:
            head = self.queue[self.head]
            self.queue[self.head] = None
            self.head += 1
            return head
        else:
            return "Error Queue Empty."
    
    def enqueue(self, item):
        if self.tail +1 <= self.capacity-1:
            self.tail += 1
            self.queue[self.tail] = item
        else:
            print("Error Capacity of queue reached.")
    
    def is_empty(self):
        return self.queue[self.head] == None

inputing = False #True
values_array = [node(0,1,None,None,None),node(1,0,None,None,None)]
count = 8
while inputing:
    print("Enter # to end")
    value = input("Enter Node: ")
    if value != "#":
        neighbours = input("Enter neighbours: 1,2,3,4/None: ")
        neighbours = neighbours.split(",")
        values_array.append(node(value, neighbours[0],neighbours[1],neighbours[2],neighbours[3]))
        count +=1
    else:
        inputing = False


Q = LinearQueue(count*4)
Q.enqueue(values_array[0])

Been_in_Q = [0]

while Q.is_empty() == False:
    current = Q.dequeue()
    for y in range(4):
        neighbour = current.neighbours()[y]
        if neighbour != None:
            been_in = False
            for x in Been_in_Q:
                if x == neighbour:
                    been_in = True
            if been_in == False:
                Q.enqueue(neighbour)
                Been_in_Q.append(neighbour)
            print(current)
            print(neighbour)
        
    print(current)
