
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.right_child = None
        self.left_child = None
    
    def add_left_child(self, other):
        self.left_child = other
        other.parent = self
    
    def add_right_child(self, other):
        self.right_child = other
        other.parent = self
    
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



choice = int(input("1. Array1 \n2. Array2 \n3. Custom Array :\n"))

if choice == 1:
    array = [37,12,81,19,26,46,51,14]
elif choice == 2:
    array = [15,19,26,7,4,13,18,16,2,9]
else:
    print("Enter each value individually (# = end of array):")
    num = input()
    Exit = False
    array = []
    while Exit == False:
        if num == "#":
            Exit = True
            print("exiting")
        else:
            array.append(num)
            num = input()
            
root = Node(array[0])

for value in array[1:]:
    parent = root
    while True:
        if value > parent.value:
            if parent.right_child == None:
                parent.add_right_child(Node(value))
                break
            else:
                parent = parent.right_child
        else:
            if parent.left_child == None:
                parent.add_left_child(Node(value))
                break
            else:
                parent = parent.left_child

print("Pre:")
root.pre_order_traversal(root)
print("")

print("Post:")
root.post_order_traversal(root)
print("")

print("In:")
root.in_order_traversal(root)
print("")
