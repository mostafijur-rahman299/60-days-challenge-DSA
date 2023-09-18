# Brute Force Approach
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        results.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return results
    

# Better With o(n^2) approach using hashmap
# nums[k] = -(nums[i] + nums[j])
results = set()

nums = [-1,0,2,1]

for i in range(len(nums)):
    has_map = []
    for j in range(i + 1, len(nums)):
        if j-1 != i:
            has_map.append(nums[j-1])

        k = -(nums[i] + nums[j])

        if k in has_map:
            results.add(tuple(sorted([nums[i], nums[j], k])))


# Two pointer optimize way

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        results = set()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while k > j:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    results.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                    while k > j and nums[j] == nums[j-1]:
                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
        return results
    
