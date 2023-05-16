from HeapPriorityQueueM import queue
from Graph import node


graph = []
graph2 = []
inputting = True

def ingraph(value):
    count = 0
    for x in graph:
        if x.value == value:
            return count
        else:
            count += 1
    return None

while inputting:
    print("Enter # to exit")
    Node = input("Enter Node: ")
    if Node != "#":
        neighbours = input("Enter neighbour/priority: ")
        neighbours = neighbours.split(",")
        for num in range(len(neighbours)):
            neighbours[num] = neighbours[num].split("/")
        
        if ingraph(Node) != None:
                this_node = graph[ingraph(Node)]
        else:
            this_node = node(Node)
            graph.append(this_node)
            graph2.append(this_node.value)

        for neighbour in neighbours:
            if ingraph(neighbour[0]) != None:
                this_neighbour = graph[ingraph(neighbour[0])]
            else:
                this_neighbour = node(neighbour[0])
                graph.append(this_neighbour)
                graph2.append(this_neighbour.value)

            this_node.give_neighbour(this_neighbour)
            this_node.give_neighbour_weight(-int(neighbour[1]))
    
    else:
        inputting = False

test = True
if test:
    for Node in graph:
        print("New node :", Node.value)
        for neighbour in Node.neighbours:
            print(neighbour)
            print(neighbour.value)
    print(graph2)


Q = queue(len(graph)+1)
Q.enqueue(graph[0], 0)
beenDQ = []
beenDQ_B = False

runold = False

if runold == True:
    print("------------")
    while Q.is_empty() == False:
        current = Q.dequeue()
        for neighbour in current[0].neighbours:
            if neighbour != None:
                for x in beenDQ:
                    if x == neighbour:
                        beenDQ_B = True

                if beenDQ_B == False:
                    beenDQ.append(neighbour)
                    num = current[0].getplaceofweight(neighbour)
                    neighbour.placeval = current[0].placeval - int(current[0].weightofneighbours[num])
                    neighbour.priority = neighbour.placeval
                    Q.enqueue(neighbour, -neighbour.priority)
                beenDQ.append(current[0])
                beenDQ_B = False
    
        print(current[0].value,  current[0].placeval)

###### new
else:
    print("------------")
    while Q.is_empty() == False:
        current = Q.dequeue()
        for neighbour in current[0].neighbours:
            if neighbour != None:
                


                for x in beenDQ:
                    if x == neighbour:
                        beenDQ_B = True

                if beenDQ_B == False:
                    beenDQ.append(neighbour)
                    num = current[0].getplaceofweight(neighbour)
                    neighbour.placeval = current[0].placeval - int(current[0].weightofneighbours[num])
                    neighbour.priority = neighbour.placeval
                    Q.enqueue(neighbour, -neighbour.priority)
                beenDQ.append(current[0])
                beenDQ_B = False
    
        print(current[0].value,  current[0].placeval)


while Q.is_empty()==False:
    current = Q.dequeue()
    for neighbour in current[0].neighbours:
        neighbour.placeval
        neighbour.priority = neighbour.placeval
        Q.enqueue(neighbour, -neighbour.priority)
