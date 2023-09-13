class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_
        
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def printf(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        
    def prepend(self, data):
        node = Node(data)
        
        if not self.head:
            self.head = node
            return
        
        temp_head = self.head
        self.head = node
        node.next = temp_head
        
    def middle(self):
        if not self.head: return
        
        pointer1 = self.head
        pointer2 = self.head
        
        while pointer1.next and pointer2 and pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            
        print("\n")
        print(pointer1.val)
        
        
list1 = LinkedList()

head = [1,2,3,4,5,6]

# list1.prepend(6)
list1.prepend(5)
list1.prepend(4)
list1.prepend(3)
list1.prepend(2)
list1.prepend(1)
list1.printf()
list1.middle()
