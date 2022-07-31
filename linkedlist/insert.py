# program for inserting a node at the front of the linked list
#node class 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkdlist:
    def __init__(self):
        self.head= None
    #inserting new node at the beginning
    def front(self, data):
        new_node= Node(data)

        new_node.next= self.head

        self.head = new_node

    #printing linkedlist 
    def printl(self):
        start= self.head
        while start:
            print(start.data, end= " ")
            start = start.next
            
if __name__ == '__main__':

    objlist = Linkdlist()

    objlist.front(7)
    objlist.front(8)
    objlist.front(9)

    objlist.printl()



# time complexity : O(n)
    

        
