class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        prefix = suffix = 0

        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[len(nums)-i -1]
            res = max(res,max(prefix,suffix))
        return res




