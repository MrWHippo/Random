
class node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None

    def insert_left_child(self, other):
        self.left_child = other
        other.parent = self
    
    def insert_right_child(self, other):
        self.right_child = other
        other.parent = self
    
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
        
    def pre_order_traversal(self, root):
        if root == None:
            return
        print(root.value)
        self.pre_order_traversal(root.left_child)
        self.pre_order_traversal(root.right_child)

    def post_order_traversal(self, root):
        if root == None:
            return
        self.post_order_traversal(root.left_child)
        self.post_order_traversal(root.right_child)
        print(root.value)
    
    def in_order_traversal(self, root):
        if root == None:
            return
        self.in_order_traversal(root.left_child)
        print(root.value)
        self.in_order_traversal(root.right_child)

#count = 0
#end = False
#rootnum = input("Enter root node: ")
#BinaryTree = node(rootnum)
#rootnode = BinaryTree
#while end == False:
#    num = int(input("1= Continue \n2= Exit"))
#    if num == 1:
#        choice = input("Enter next node (in format: Direction,Direction......,Value): ")
#        print(choice)
#        choice = choice.split(",")
#        print(choice)
#        parent = BinaryTree
#        for x in choice:
#            count += 1
#            if count == 1:
#                if x == "L":
#                    parent = parent.get_left_child()
#                elif x == "R":
#                    parent = parent.get_right_child()
#                else:
#                    print(choice[-2])
#                    if choice[-2] == "L":
#                        parent.insert_left_child(node(choice[-1]))
#                    else:
#                        parent.insert_right_child(node(choice[-1]))
#
#    else:
#       end = True
#print("pre:")
#BinaryTree.pre_order_traversal(rootnode)
#print("'''''''")
#parent.pre_order_traversal(rootnode)
#print("")
#
#print("post:")
#BinaryTree.post_order_traversal(rootnode)
#print("")
#
#print("in:")
#BinaryTree.in_order_traversal(rootnode)
#print("")

choice = int(input("1/2: "))

if choice == 1:
    BinaryTree = node(100)
    node1 = node(87)
    node2 = node(193)
    node3 = node(63)
    node4 = node(180)
    node5 = node(200)
    node6 = node(1)
    node7 = node(68)
    node8 = node(185)
    node9 = node(210)

    BinaryTree.insert_left_child(node1)
    BinaryTree.insert_right_child(node2)
    node1.insert_left_child(node3)
    node3.insert_left_child(node6)
    node3.insert_right_child(node7)
    node2.insert_left_child(node4)
    node4.insert_right_child(node8)
    node2.insert_right_child(node5)
    node5.insert_right_child(node9)
else:
    BinaryTree = node("A")
    nodeB = node("B")
    nodeC = node("C")
    nodeD = node("D")
    nodeE = node("E")
    nodeF = node("F")
    nodeG = node("G")
    nodeH = node("H")
    nodeI = node("I")
    nodeJ = node("J")
    nodeK = node("K")
    nodeL = node("L")
    
    BinaryTree.insert_left_child(nodeB)
    BinaryTree.insert_right_child(nodeC)
    nodeB.insert_right_child(nodeD)
    nodeD.insert_left_child(nodeJ)
    nodeJ.insert_left_child(nodeK)
    nodeJ.insert_right_child(nodeL)
    nodeC.insert_right_child(nodeF)
    nodeF.insert_left_child(nodeH)
    nodeH.insert_right_child(nodeI)

print("pre:") # tested and working
BinaryTree.pre_order_traversal(BinaryTree)
print("")

print("post:") # tested and not working
BinaryTree.post_order_traversal(BinaryTree)
print("")

print("in:") # tested and not working
BinaryTree.in_order_traversal(BinaryTree)
print("")
