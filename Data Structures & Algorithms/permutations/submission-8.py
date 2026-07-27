class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)

        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm[:])  # Make a copy of the current permutation
                return
            
            for i in range(len(nums)):
                if not pick[i]: 
                    perm.append(nums[i])
                    pick[i] = True
                    
                    backtrack(perm)  # Direct call (no self)
                    
                    # Backtrack step
                    perm.pop()
                    pick[i] = False

        backtrack([])
        return res