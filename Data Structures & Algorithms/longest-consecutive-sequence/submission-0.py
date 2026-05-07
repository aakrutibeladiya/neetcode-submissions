class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        largest = 0
        for el in nums:
            #check if el is starting point of the consecutivelist 
            if (el-1) not in numsSet:
                length = 0
                while (el+length) in numsSet:
                    length += 1
                largest = max(largest, length)
        return largest