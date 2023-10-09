## 20. Valid Parentheses

```
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
    Input: s = "()"
    Output: true
```

### Solution

```python
class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack
    
s = Solution()
s.isValid("([])")
```

#### Time & Space Complexity Analysis
```
*Time Complexity*:
    * We uses a single pass through the input `s` of length `n`.In the worst case,
    it will visit all characters in the string once(it performs n times operation). 
    For each character, it performs constant-time operations(pushing onto the stack, 
    popping from the stack, and comparisons)

    therefore, the time complexity of the code is O(n), where n is the length of the string.

*Space Complexity*:
    * Space Complexity depends on the space used by the stack, which can grow at most to the 
    size of the input string in the worst case. In the worst case, when all opening parentheses
    are followed by closing parentheses, in the correct order, the stack will grow to the size
    of the input string.

    therefore, the space complexity of the code is O(n), where n is the length of the string `s`.
```
