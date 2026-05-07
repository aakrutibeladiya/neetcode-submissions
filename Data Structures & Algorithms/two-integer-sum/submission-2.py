class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        discoveredNums = {}
        for i,val in enumerate(nums):
            if target - val in discoveredNums:
                return [discoveredNums[target-val],i]
            else: 
                discoveredNums[val] = i 
        return []

