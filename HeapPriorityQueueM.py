class queue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [(None,None)] * capacity
        self.head = 1
        self.tail = 0
        self.count = 0
    
    def enqueue(self, value, priority):
        if self.tail + 1 <= self.capacity:
            self.tail += 1
            self.count += 1
            self.queue[self.tail] = (value, priority)
            location = self.tail
            if self.queue[location//2][1] != None:
                while self.queue[location][1] > self.queue[location//2][1]:
                    temp = self.queue[location//2]
                    self.queue[location//2] = self.queue[location]
                    self.queue[location] = temp
                    location //= 2
                    if self.queue[location//2][1] == None:
                        break

    def dequeue(self):
        dequeuevalue = self.queue[1]
        if dequeuevalue[1] == None:
            return "Error, Nothing in Queue."
        self.queue[1] = self.queue[self.tail]
        self.queue[self.tail] = (None, None)
        location = 1
        self.tail -= 1
        if self.queue[location*2][1] != None:
            while self.queue[location][1] < self.queue[self.__maxchild(location)][1]:
                childlocation = self.__maxchild(location)
                temp = self.queue[childlocation]
                self.queue[childlocation] = self.queue[location]
                self.queue[location] = temp
                location = childlocation
                if self.queue[location*2][1] == None:
                    break
        self.count -= 1
        return dequeuevalue
    
    def __maxchild(self, location):
        child1= self.queue[location*2]
        child2 = self.queue[location*2 + 1]
        if child2[1] == None:
            return location*2
        if child1[1] > child2[1]:
            return location*2
        else:
            return (location*2 +1)

    def top(self):
        return self.queue[1]

    def numinqueue(self):
        return self.count

    def printqueue(self):
        return self.queue
    
    def is_empty(self):
        return self.numinqueue() == 0