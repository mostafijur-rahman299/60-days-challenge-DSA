## 141. Linked List Cycle
```
Given head, the head of a linked list, determine if the linked list has a cycle in it.

Example:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
```

### Solution

```python
def hasCycle(head):
    slow=head
    fast=head
    while slow and fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True

    return False   
```

#### Time & Space Complexity Analysis
```
Time Complexity:
    The time complexity of this code is O(n), where 'n' is the number of nodes in the linked list. 
    The slow pointer moves through the list once, and the fast pointer moves through the list twice as fast. 
    If there is a cycle, the fast pointer will eventually catch up to the slow pointer, which occurs after 
    at most 'n' iterations. In the absence of a cycle, the loop will terminate when the fast pointer 
    reaches the end of the linked list, also in O(n) time.

Space Complexity:
    The space complexity of this code is O(1), which means it uses a constant amount of extra space. 
    It uses two pointers (slow and fast) to traverse the linked list, but the number of additional 
    variables is not dependent on the size of the linked list. It doesn't use any data structures 
    that grow with the input size.
```
