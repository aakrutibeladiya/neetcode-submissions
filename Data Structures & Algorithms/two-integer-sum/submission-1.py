class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # all the seen elements
        for i,v in enumerate(nums):
            comp = target - v
            if comp in seen:
                return [seen[comp],i]
            seen[v] = i 

    ## brute force
    #   def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i,j]