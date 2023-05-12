from HeapPriorityQueue import queue
from Graph import node


graph = []
inputting = True

def ingraph(value):
    count = 0
    for x in graph:
        if x == value:
            return
        else:
            count += 1
    return None

while inputting:
    Node = input("Enter Node: ")
    neighbours = input("Enter neighbour/priority: ")
    neighbours = neighbours.split(",")
    for num in range(len(neighbours)):
        neighbours[num] = neighbours[num].split("/")
    
    this_node = node(Node)
    for neighbour in neighbours:
        this_neighbour = node(neighbour[0])
        if ingraph(this_neighbour):
            



Queue = queue(...)
    
