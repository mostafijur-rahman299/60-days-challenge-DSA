class MinStack:

    def __init__(self):
        self.stack = []
        self.global_min = None

    def push(self, val: int) -> None:
        if not stack or self.global_min is None:
            self.global_min = val
        elif val < self.global_min:
            self.global_min = val
        
        self.stack.append(Stack(val, self.global_min))

    def pop(self) -> None:
        if not self.stack: return None
        self.stack.pop()
        
        if self.stack:
            self.global_min = self.stack[len(self.stack)-1].local_min
        else:
            self.global_min = None

    def top(self) -> int:
        if not self.stack: return None
        item = self.stack[len(self.stack)-1]
        return item.val

    def getMin(self) -> int:
        return self.global_min
    

class Stack:
    def __init__(self, val, local_min):
        self.val = val
        self.local_min = local_min
        
        
stack = MinStack()

stack.push(0)
stack.push(12)
stack.push(1)
stack.push(19)

stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()

# stack.top()

stack.getMin()



