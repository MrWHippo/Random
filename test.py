from HeapPriorityQueueM import queue

Q = queue(5)

Q.enqueue("A",0)
Q.enqueue("B",-2)
Q.enqueue("C",-6)
Q.enqueue("D",-1)
Q.printqueue()
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
