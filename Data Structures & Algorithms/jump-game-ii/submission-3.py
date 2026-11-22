class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        curr = 0
        jumps =0

        for i in range(len(nums)-1):
            furthest = max(furthest, i+nums[i])
            if curr == i:
                jumps += 1
                curr = furthest
        return jumps