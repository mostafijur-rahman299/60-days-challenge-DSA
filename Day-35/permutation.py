from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perms(nums, curr, answer):
            if len(nums) == 0:
                answer.append(curr.copy())
                
            for item in nums:
                curr.append(item)
                new_nums = [x for x in nums if x != item]
                perms(new_nums, curr, answer) 
                curr.pop()
            return answer
        return perms(nums, [], [])
    