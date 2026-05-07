class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = []
        for num in nums:
            if num in uniqueSet:
                return True
            uniqueSet.append(num)
        return False