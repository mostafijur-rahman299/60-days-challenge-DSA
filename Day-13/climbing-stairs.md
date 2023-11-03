## 70. Climbing Stairs
```
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
```

### Solution

```python
def climbStairs(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return b
```

#### Time & Space Complexity analysis
```
Time Complexity:
    The function uses a loop that iterates n times, where n is the input parameter.
    Within each iteration of the loop, there are constant time operations (assignment and addition) that do not depend on the input size.
    As a result, the time complexity is linear in terms of n.

Space Complexity:
    The function uses only a constant amount of extra space regardless of the input size.
    It maintains two variables a and b, but these are not dependent on n, so the space complexity is constant.
```
