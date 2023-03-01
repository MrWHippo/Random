

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
    
    def front(self):
        return self.queue[self.head]
    
    def is_empty(self):
        return self.queue[self.head] == None

    def printqueue(self):
        return self.queue

length = int(input("Enter length of queue: "))
queue = LinearQueue(length)

Exit = False
while Exit == False:
    print("1: Enqueue \n2: Dequeue \n3: Check if Queue is Empty \n4: Get Item at Front of Queue \n5: Print Queue \n6: Exit")
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
    
    else:
        Exit = True
