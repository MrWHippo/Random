
class NaivePriorityQueue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [(None, None)]* capacity
        self.head = 0
        self.tail = -1
        self.count = 0
    
    def enqueue(self, value, priority):
        self.tail += 1
        self.queue[self.tail] = (value, priority)
        self.count += 1

    def highestpriority(self):
        highestvalue = 0
        highestposition = 0

        for x in range(self.count):
            if highestvalue < self.queue[x][1]:
                highestvalue = self.queue[x][1]
                highestposition = x
            
        return highestposition

    def __fixqueue(self):
        emptyvalue = False
        for x in range(self.capacity):
            if self.queue[x][0] == None:
                emptyvalue = True
            else:
                if emptyvalue == True:
                    self.queue[x-1] = self.queue[x]
                    self.queue[x] = (None, None)
        pass

    def dequeue(self):
        position = self.highestpriority()
        value = self.queue[position][0]
        self.queue[position] = (None, None)
        self.__fixqueue()
        return value

    def top(self):
        position = self.highestpriority()
        return self.queue[position]
    
    def printqueue(self):
        print(self.queue)
    

PriorityQueue = NaivePriorityQueue(5)

Exit = False
while Exit == False:
    print("1: Enqueue \n2: Dequeue \n3: Get Item at the Top of the Queue \n4: Print Queue \n5: Exit")
    key = int(input("What would you like to do?: "))
    if key == 1:
        print("What would you like to Enqueue?")
        Value = input("Enter Value: ")
        Priority = int(input("Enter Priority: "))
        PriorityQueue.enqueue(Value, Priority)

    elif key == 2:
        print(PriorityQueue.dequeue())
    
    elif key == 3:
        print(PriorityQueue.top())
    
    elif key == 4:
        print(PriorityQueue.printqueue())

    else:
        Exit = True