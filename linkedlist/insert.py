# program for inserting a node at the front of the linked list
#node class 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
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

    llist = Linkedlist()

    llist.front(7)
    llist.front(8)
    llist.front(9)

    llist.printl()



# time complexity : O(n)
    

        
