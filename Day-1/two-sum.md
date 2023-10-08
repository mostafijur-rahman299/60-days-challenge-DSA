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

1. Initialize an empty list indices to store the indices of the two numbers that add up to the target.

2. Iterate through the nums list using two nested loops. The outer loop runs from index i equal to 0 to len(nums)-1, and the inner loop runs from index j equal to i+1 to len(nums)-1. This ensures that you are considering pairs of distinct elements in the nums list.

3. Inside the inner loop, check if the sum of nums[i] and nums[j] equals the target. If it does, append the indices i and j to the indices list and break out of the inner loop. This is done to find the first valid pair of indices that sum up to the target.

4. After breaking out of the inner loop, the outer loop continues to search for other pairs that sum up to the target. If no more pairs are found, the method returns the indices list.

5. Finally, an instance of the Solution class is created (i.e., s) and the twoSum method is called with the input [2, 7, 11, 15] and 17. In this case, the method should return [0, 3], because nums[0] + nums[3] equals 2 + 15, which is equal to the target of 17.

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

1. Initialize an empty dictionary numMap to store the values from the nums list as keys and their corresponding indices as values.

2. Iterate through the nums list using a for loop with an index i. For each element nums[i], calculate the complement as target - nums[i]. The complement represents the value that, when added to nums[i], will result in the target.

3. Check if the complement is already in the numMap (i.e., it is one of the values seen so far in the nums list). If it is, this means we have found a pair of numbers whose sum equals the target. In this case, return a list containing the indices [numMap[complement], i], where numMap[complement] is the index of the previously seen number that, when added to the current number at index i, equals the target.

4. If the complement is not in the numMap, add the current number nums[i] to the numMap with its index i as the value. This allows us to store the numbers and their indices as we iterate through the list.

5. If the loop completes without finding a pair of numbers that sum up to the target, return an empty list [].

6. Finally, an instance of the Solution class is created (i.e., s), and the twoSum method is called with the input [2, 7, 11, 15] and 17. In this case, the method should return [0, 3], because nums[0] + nums[3] equals 2 + 15, which is equal to the target of 17.

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

1. Create a list called numsIndex using list comprehension, where each element is a tuple (num, i) representing the value num from the original nums list and its index i in the original list. This step pairs each number with its index in the list for later reference.

2. Sort the numsIndex list in ascending order based on the values (num) of the tuples. This step is important because it allows us to efficiently find pairs of numbers that sum up to the target value.

3. Initialize two pointers, left and right, which initially point to the beginning and end of the sorted numsIndex list, respectively.

4. Enter a while loop that continues as long as left is less than right.

5. Calculate the sum num_sum of the values at the left and right pointers in the sorted numsIndex list (numsIndex[left][0] and numsIndex[right][0], respectively).

6. Check if num_sum is equal to the target value. If it is, this means you've found a pair of numbers whose sum equals the target, so return a list containing the indices [numsIndex[left][1], numsIndex[right][1]], which correspond to the indices of the original nums list.

7. If num_sum is less than the target, increment the left pointer to move towards larger values in the sorted list.

8. If num_sum is greater than the target, decrement the right pointer to move towards smaller values in the sorted list.

9. If the while loop completes without finding a pair of numbers that sum up to the target, return an empty list [].

```python
def twoSum(nums, target):
    numsIndex = [(num, i) for i, num in enumerate(nums)]
    numsIndex.sort()

    left, right = 0, len(nums) - 1

    while left < right:
        num_sum = numsIndex[left][0] + numsIndex[right][0]
        
        if num_sum == target:
            return [numsIndex[left][1], numsIndex[right][1]]
        elif num_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

#### Time & Space complexity analysis
```
Time complexity of this solution is O(N) where N is the number of nums.

Space complexity of this solution is O(N) where N is the number of nums.
```
