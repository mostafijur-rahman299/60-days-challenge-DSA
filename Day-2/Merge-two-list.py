class LinkedNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_item(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next
        
    def insert_item(self, val):
        node = LinkedNode(val)
        if not self.head:
            self.head = node
            return
        
        temp_head = self.head
        self.head = node
        node.next = temp_head
        
    def mergeTwoLists(self, list1, list2):
        
        current1 = list1
        
        while current1:
            current2 = list2
            
            while current2:
                if current1.val < current2.val:
                    
                elif current1.val >= current2.val and current1.next and current1.next.val < current2.val:
                    pass
                elif not current1.next:
                    pass
                else:
                    break
        
        
        
list1 = [1,2,4]
list2 = [1,3,4]

link_list_1 = LinkedList()
link_list_1.insert_item(4)
link_list_1.insert_item(2)
link_list_1.insert_item(1)

link_list_1.print_item()

link_list2 = LinkedList()
link_list2.insert_item(4)
link_list2.insert_item(3)
link_list2.insert_item(1)

link_list2.print_item()
