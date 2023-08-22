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

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        return []
