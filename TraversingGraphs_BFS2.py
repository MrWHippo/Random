from Graph import node

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
    
    def printqueue(self):
        print(self.queue)


def ingraph(searchval, graph):
    count = -1
    for value in graph:
        count +=1
        if value.value == searchval:
            return count
    return None

inputing = True
graph = []


while inputing:
    print("Enter # to end")
    value = input("Enter Node: ")
    if value != "#":
        neighbours = input("Enter neighbours: ")
        neighbours = neighbours.split(",")

        if ingraph(value, graph) == None:
            thisNode = node(value)
            graph.append(thisNode)
        else:
            thisNode = graph[ingraph(value, graph)]
            
        for neighbour in neighbours:
            if ingraph(neighbour, graph) == None:
                neighbour_node = node(neighbour)
                graph.append(neighbour_node)
            else:
                neighbour_node = graph[ingraph(value,graph)]

            thisNode.give_neighbour(neighbour_node)
    else:
        inputing = False



Q = LinearQueue(len(graph)+1)
Q.enqueue(graph[0])
Been_in_Q = [graph[0]]
graph[0].placeval = 0


while Q.is_empty() == False:
    current = Q.dequeue()
    for neighbour in current.neighbours:
        if neighbour != None:
            been_in = False
            for x in Been_in_Q:
                if x == neighbour:
                    been_in = True
            if been_in == False:
                Q.enqueue(neighbour)
                Been_in_Q.append(neighbour)
                neighbour.placeval = 1 + current.placeval
  
    print(current.value, current.placeval)
