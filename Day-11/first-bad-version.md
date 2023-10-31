## 278. First Bad Version
```
You are a product manager and currently leading a team to develop a new product. Unfortunately, 
the latest version of your product fails the quality check. Since each version is developed based 
on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:
    Input: n = 5
    Output: 4
```

### Solution

```python
def firstBadVersion(n):
    s = 1
    e = n
    while s < e:
        m = int(s + (e-s)/2)
        if(isBadVersion(m)):
            e = m
        else:
            s = m + 1
    return s
```

#### Time & Space Complexity Analysis
```
Time Complexity:
    The while loop runs until the start (s) is less than the end (e), and with each iteration, 
    the range is halved. Since each iteration reduces the range by half, it takes O(log n) 
    iterations to converge to the first bad version. The time complexity of the binary search 
    algorithm is O(log n), where "n" is the input size (the range of versions).

Space Complexity:
    The code uses a constant amount of extra space, regardless of the input size.
    It only creates a few integer variables (s, e, m) and does not use any additional 
    data structures that depend on the input size. The space complexity is O(1) or constant space.
```

