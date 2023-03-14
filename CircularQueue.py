
class CircularQueue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.head = 0
        self.tail = -1
        self.count = 0
    
    def dequeue(self):
        head = self.queue[self.head]
        self.queue[self.head] = None
        self.count -= 1
        if self.head +1 == self.capacity:
            self.head = 0
        else:
            self.head += 1
        return head
    
    def enqueue(self, item):
        if self.tail < self.capacity:
            self.tail += 1
            self.count += 1
            self.queue[self.tail] = item
        elif self.queue[0] == None:
            self.tail = 0
            self.count += 1
            self.queue[self.tail] = item
        else:
            print("Error Capacity of queue reached.")
    
    def front(self):
        return self.queue[self.head]
    
    def is_empty(self):
        return self.count == 0

    def printqueue(self):
        return self.queue

    def numvaluesinqueue(self):
        return self.count
length = int(input("Enter length of queue: "))
queue = CircularQueue(length)

Exit = False
while Exit == False:
    print("1: Enqueue \n2: Dequeue \n3: Check if Queue is Empty \n4: Get Item at Front of Queue \n5: Print Queue \n6: Check How Many Values in Queue \n7: Exit")
    key = int(input("What would you like to do?: "))
    if key == 1:
        value = input("What would you like to Enqueue?: ")
        queue.enqueue(value)

    elif key == 2:
        print(queue.dequeue())
    
    elif key == 3:
        print(queue.is_empty())
    
    elif key == 4:
        print(queue.front())
    
    elif key == 5:
        print(queue.printqueue())
    
    elif key == 6:
        print(queue.numvaluesinqueue())
    else:
        Exit = True