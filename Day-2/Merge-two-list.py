class LinkedNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_
        

class LinkedList:
    def __init__(self):
        self.head = None
    
    @staticmethod
    def print_item(head):
        current = head
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
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2
        
        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = seek
        
        while seek and target:
            while seek.next and seek.next.val < target.val:
                seek = seek.next
            seek.next, target = target, seek.next
            seek = seek.next
        return head
    
    def mergeTwoLists2(self, list1, list2):
        cur = dummy = LinkedNode()
        
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
                
#                 print("list1===", list1.val)
#                 print("cur====", cur.val)
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
                
        
        
        
list1 = [1,2,4]
list2 = [1,3,4]

link_list_1 = LinkedList()
link_list_1.insert_item(4)
link_list_1.insert_item(2)
link_list_1.insert_item(1)

LinkedList.print_item(link_list_1.head)

print("======================")

link_list2 = LinkedList()
link_list2.insert_item(40)
link_list2.insert_item(30)
link_list2.insert_item(2)

LinkedList.print_item(link_list2.head)

print("======================")

merge_head = link_list_1.mergeTwoLists(link_list_1.head, link_list2.head)

LinkedList.print_item(merge_head)

print("======================")
