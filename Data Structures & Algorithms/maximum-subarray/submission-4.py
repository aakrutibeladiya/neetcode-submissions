class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningSum = 0
        maxSub =  nums[0]
        for i in nums: 
            if runningSum < 0:
                runningSum =0
            runningSum += i
            maxSub = max(maxSub, runningSum)
        return maxSub


