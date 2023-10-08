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
Time Complexity:

The code uses two nested loops to iterate through the nums list:

The outer loop runs from i = 0 to i = n-1, where n is the length of the nums list.

The inner loop runs from j = i + 1 to j = n-1.

Within the inner loop, there's a check to see if nums[i] + nums[j] equals the target. This check involves constant time operations.

So, the total number of iterations in the nested loops is roughly proportional to n(n-1)/2, which is O(n^2) in the worst case. Therefore, the time complexity of this code is O(n^2), where n is the length of the nums list.

Space Complexity:

The space complexity primarily depends on the indices list, which stores the indices of the two numbers that sum up to the target.

The indices list will contain at most two elements, as it stores the indices of the two numbers that sum up to the target.

Other than the indices list, there are no additional data structures created that depend on the size of the input nums list.

So, the space complexity of this code is O(1), as the amount of additional memory used does not depend on the size of the input list. The indices list has a fixed maximum size of 2.

In summary:

Time Complexity: O(n^2) (quadratic time complexity due to nested loops)
Space Complexity: O(1) (constant space complexity)
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
Time Complexity:

The code uses a single pass through the nums list to find the pair of numbers that sum up to the target:

The for loop iterates through the nums list once, from index 0 to n-1, where n is the length of the nums list.
Inside the loop:

The calculation of the complement (i.e., target - nums[i]) and the dictionary look-up (i.e., complement in numMap and numMap[complement]) are constant-time operations.
Therefore, the overall time complexity of this code is O(n), where n is the length of the nums list. It's a linear time complexity because the number of operations scales linearly with the size of the input list.

Space Complexity:

The space complexity depends on the additional data structures used in the code:

numMap: This dictionary stores the numbers from the nums list as keys and their corresponding indices as values. In the worst case, it can store all n unique numbers from the nums list. Therefore, the space complexity for numMap is O(n) in the worst case.

The list returned, [numMap[complement], i], also has a space complexity of O(2) or O(1), as it contains a fixed number of elements (two elements).

The dominant factor in space complexity is the numMap dictionary, so the overall space complexity of this code is O(n) in the worst case, where n is the length of the nums list.

In summary:

Time Complexity: O(n) (linear time complexity)
Space Complexity: O(n) (linear space complexity)
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
Time Complexity:

Building the numsIndex list: The code starts by creating a list of tuples (num, i) where num is the value from the nums list, and i is its index using a list comprehension. This step has a time complexity of O(n) because it iterates through the entire nums list.

Sorting the numsIndex list: The numsIndex list is sorted using the .sort() method. Sorting a list of n elements typically has a time complexity of O(n*log(n)).

The while loop: The main work is done within the while loop, which continues as long as left < right. Inside the loop, there are no nested loops or additional significant operations that depend on the size of the input, except for the constant-time comparisons and updates.

Overall, the dominant factor affecting the time complexity is the sorting step, which has a time complexity of O(nlog(n)). Therefore, the overall time complexity of this code is O(nlog(n)), where n is the length of the nums list.

Space Complexity:

numsIndex list: This list is created to store tuples, but it does not significantly contribute to the space complexity since it only contains references to the original elements in the nums list. The space complexity for this list is O(n).

Other than the numsIndex list, there are no additional data structures created that depend on the size of the input nums list.

So, the overall space complexity of this code is O(n) due to the numsIndex list.

In summary:

Time Complexity: O(n*log(n)) (due to the sorting step)
Space Complexity: O(n) (linear space complexity)
```
