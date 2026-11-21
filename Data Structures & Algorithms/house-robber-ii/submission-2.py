class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def run(start,end): 
            memo = [0] * len(nums)  
            def dfs(i):
                if i >= end:
                    return 0
                if memo[i]:
                    return memo[i]
                memo[i] = max(dfs(i+1), nums[i]+ dfs(i+2))
                return memo[i]
            return dfs(start)
            
        
        return max(run(0,len(nums)-1),run(1,len(nums)))
            