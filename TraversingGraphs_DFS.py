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
        for x in verlist:
            if x[0] == None:
                x[0] = float("inf")
        verlist = bubble_sort_2D(verlist)
    print(verlist)

def printbysortedexit():
    verlist = []
    for vertex in graph:
        verlist.append([vertex.exit_time, vertex.value])
        for x in verlist:
            if x[0] == None:
                x[0] = float("inf")
        verlist = bubble_sort_2D(verlist)
    print(verlist)

def ingraph(searchval, graph):
    count = -1
    for value in graph:
        count +=1
        if value.value == searchval:
            return count
    return None
        

graph = []
inputting = True

while inputting == True:
    print("# to stop inputting.")
    value = input("Enter vertex: ")
    if value != "#":
        neighbours = input("Enter neighbours 1,2,3.... : ")
        neighbours = neighbours.split(",")

        if ingraph(value, graph) == None:
            thisNode = node(value)
            graph.append(thisNode)
        else:
            thisNode = graph[ingraph(value,graph)]
            
        for neighbour in neighbours:
            if ingraph(neighbour, graph) == None:
                neighbour_node = node(neighbour)
                graph.append(neighbour_node)
            else:
                neighbour_node = graph[ingraph(value,graph)]

            thisNode.give_neighbour(neighbour_node)
    else:
        inputting = False
            

graph[0].entry_time = 1
dfs(graph)
print("Entry")
printbysortedentry()
print("Exit")
printbysortedexit()
