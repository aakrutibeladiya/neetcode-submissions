class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers)-1
        left = 0
        while left <= right:
            if (numbers[left] + numbers[right]) == target:
                return [left+1,right+1]
            if (numbers[left] + numbers[right]) > target:
                right = right - 1 
            else:
                left = left + 1
        return []