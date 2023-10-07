## 1. Two Sum

```
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Solution 1 (Brute Force)
```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j]) == target:
                    indices.append(i)
                    indices.append(j)
                    break
        return indices
    
s = Solution()
s.twoSum([2,7,11,15], 17)
```

#### Time & Space complexity analysis
```
Time complexity of this solution is O(N^2) where N is the number of nums.

1. O(N) * O(N) = O(N^2)

Space complexity of this solution is O(1).
```

### Solution 2 (Hash Table)

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        return []

s = Solution()
s.twoSum([2,7,11,15], 17)
```

#### Time & Space complexity analysis
```
Time complexity of this solution is O(N) where N is the number of nums.

Space complexity of this solution is O(N) where N is the number of nums.
```

### Solution 3 (Two pointer)

```python
def twoSum(nums, target):
    numsWithIndex = [(num, i) for i, num in enumerate(nums)]
    numsWithIndex.sort()

    left, right = 0, len(nums) - 1

    while left < right:
        num_sum = numsWithIndex[left][0] + numsWithIndex[right][0]
        
        if num_sum == target:
            return [numsWithIndex[left][1], numsWithIndex[right][1]]
        elif num_sum < target:
            left += 1
        else:
            right -= 1
    return []  # No solution found!
```

#### Time & Space complexity analysis
#### Time & Space complexity analysis
```
Time complexity of this solution is O(N) where N is the number of nums.

Space complexity of this solution is O(N) where N is the number of nums.
```
