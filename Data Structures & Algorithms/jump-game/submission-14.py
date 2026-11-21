class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1 # 0 last index

        # [1,2,0,1,0] i = at 1 from end
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
            

