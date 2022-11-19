#binary search should be sorted in asceding order or descending order

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

    def printtree(self):
        print(self.val)

                
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)


root.printtree()

Node(20).printtree()
