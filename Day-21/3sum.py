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


