## 21. Merge Two Sorted Lists
```
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing 
together the nodes of the first two lists.

Return the head of the merged linked list.

Example:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
```

### Solution

```python
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
```
### Time & Space Complexity (01 solution)
```
*Time complexity*:
    1. The while loop that iterates through the linked lists will run until both list1 and list2 are 
        completely merged. In the worst case, it will run until the end of the longer of the two lists.
    2. Inside the while loop, there are constant time operations, such as comparisons and assignments.

    The time complexity of this code is O(N + M), where N is the length of list1 and M is the length of list2. This is because need to traverse both lists once to merge them.

*Space complexity*:
    * The space complexity of the code is O(1), which means it uses a constant time amount of additional memory regardless of the input list sizes. This is because the code modifies the
    input linked lists in place and does not create any new data structures that depend on the
    size. It only uses a few variables (see, target, head) that do not depend on the input size.
```

### Time & Space Complexity (02 solution)
```
*Time complexity*:
    1. The time complexity of the code is O(N + M), where N is the length of list1 and M is the length of list2. In the while loop, you iterate through both lists exactly once, comparing 
    and merging elements in sorted manner. Since each element from both lists is examined once, 
    the time complexity of the code is linear with respect to the combined length of the two lists.

*Space Complexity*:
    The space complexity of this code is O(1), which means it uses a constant amount of additional memory. This is because it does not create any new data structures or allocate additional memory that depends on the input size. It uses a few variables (cur, dummy) to manage the linked list traversal, but the number of these variables remains constant, regardless of the input size. The merging is done in-place, so there are no new data structures created.
```
