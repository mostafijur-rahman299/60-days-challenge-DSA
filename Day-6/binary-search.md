## 704. Binary Search
```
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
```


### Solution

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    
s = Solution()
s.search([2,3,4,5], 3)
```
#### Time and Space Complexity Analysis
```
Time Complexity:
    Time complexity: O(logn) - Since binary search reduces the search 
    space by half at each step, the maximum number of iterations required to find 
    the target is log base 2 of n, where n is the size of the array. 
    
    Therefore, the time complexity of binary search is O(logn).

Space Complexity:
    Space complexity: O(1) - Binary search only uses a constant amount of 
    additional space for the two pointers and the middle index variable, 
    so the space complexity is O(1).
```
