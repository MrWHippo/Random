from HeapPriorityQueueM import queue
from Graph import node

test = 1
if test == 1:
    Q = queue(10)

    A = node("A")
    B = node("B")
    C = node("C")
    D = node("D")

    A.give_neighbour(B)
    A.give_neighbour_weight(-60)

    A.give_neighbour(C)
    A.give_neighbour_weight(-71)

    ##
    B.give_neighbour(A)
    B.give_neighbour_weight(-60)

    B.give_neighbour(C)
    B.give_neighbour_weight(-33)

    B.give_neighbour(D)
    B.give_neighbour_weight(-20)

    ##
    C.give_neighbour(A)
    C.give_neighbour_weight(-71)

    C.give_neighbour(B)
    C.give_neighbour_weight(-33)

    C.give_neighbour(D)
    C.give_neighbour_weight(-2)

    ##
    D.give_neighbour(B)
    D.give_neighbour_weight(-20)

    D.give_neighbour(C)
    D.give_neighbour_weight(-2)

    Q.enqueue(A,0)
    #Q.enqueue(B,-2)
    #Q.enqueue(C,-6)
    #Q.enqueue(D,-1)

    while Q.is_empty()==False:
        current = Q.dequeue()
        if current[0].checkfinal() == False:
            current[0].placeval = -current[1]
            current[0].final = True
            for neighbour in current[0].neighbours:
                num = current[0].getplaceofweight(neighbour)
                neighbour.placeval = current[0].placeval - int(current[0].weightofneighbours[num])
                neighbour.priority = neighbour.placeval
                Q.enqueue(neighbour, -neighbour.priority)
        
            print(current[0].value,  current[0].placeval)


