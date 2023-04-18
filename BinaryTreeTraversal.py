

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
        self.pre_order_traversal(root.left_child)
        self.pre_order_traversal(root.right_child)
        print(root.value)
    
    def in_order_traversal(self, root):
        if root == None:
            return
        self.pre_order_traversal(root.left_child)
        print(root.value)
        self.pre_order_traversal(root.right_child)
        
count = 0
end = False
rootnode = input("Enter root node: ")
BinaryTree = node(rootnode)
while end == False:
    num = int(input("1= Continue \n2= Exit"))
    if num == 1:
        choice = input("Enter next node (in format: Direction,Direction......,Value): ")
        print(choice)
        choice = choice.split(",")
        print(choice)
        parent = BinaryTree
        for x in choice:
            count += 1
            if count == 1:
                if x == "L":
                    parent = parent.get_left_child()
                elif x == "R":
                    parent = parent.get_right_child()
                else:
                    print(choice[-2])
                    if choice[-2] == "L":
                        parent.insert_left_child(node(choice[-1]))
                    else:
                        parent.insert_right_child(node(choice[-1]))

    else:
        end = True

print("pre:")
BinaryTree.pre_order_traversal(node(rootnode))
print("'''''''")
parent.pre_order_traversal(BinaryTree)
print("")

print("post:")
BinaryTree.post_order_traversal(BinaryTree)
print("")

print("in:")
BinaryTree.in_order_traversal(BinaryTree)
print("")
