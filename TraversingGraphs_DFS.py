import time
from Graph import node
from BubbleSortM import bubble_sort_2D


def visit(vertex):
    vertex.entry_time = time.time()
    for neighbour in vertex.neighbours:
        if neighbour.entry_time != None:
            neighbour.parent = vertex
            visit(neighbour)
    vertex.exit_time = time.time()


def dfs(Graph):
    for vertex in Graph:
        if vertex.entry_time != None:
            visit(vertex)

def printbysortedentry():
    verlist =[]
    for vertex in graph:
        verlist.append([vertex.entry_time, vertex.value])
        verlist = bubble_sort_2D(verlist)
    print(verlist)

def printbysortedexit():
    verlist = []
    for vertex in graph:
        verlist.append([vertex.exit_time, vertex.value])
        verlist = bubble_sort_2D(verlist)
    print(verlist)
        

graph = []
inputting = True

while inputting == True:
    print("# to stop inputting.")
    value = input("Enter vertex: ")
    if value != "#":
        neighbours = input("Enter neighbours 1,2,3.... : ")
        neighbours = neighbours.split(",")
        thisNode = node(value)
        graph.append(thisNode)
        for neighbour in neighbours:
            neighbour_node = node(neighbour)
            notingraph = True
            for x in graph:
                if x == neighbour:
                    notingraph = False
            if notingraph == True:
                graph.append(neighbour_node)
            else:
                notingraph = True
            thisNode.give_neighbour(neighbour_node)
    else:
        inputting = False
            

graph[0].entry_time = 1
dfs(graph)
print("Entry")
printbysortedentry()
print("Exit")
printbysortedexit()
