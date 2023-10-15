def subsets(nums):
    res = []
    
    subset = []
    
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        
        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        
        # decision Not to include nums[i]
        subset.pop()
        dfs(i + 1)
    dfs(0)
    return res

subsets([1,2,3])
