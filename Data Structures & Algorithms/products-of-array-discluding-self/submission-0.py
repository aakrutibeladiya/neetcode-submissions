
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixAr = [1] * len(nums)
        sufAr = [1] * len(nums)
        finalar = []
        for i in range(len(nums)):
            j = 0
            while i > j:
                sufAr[j] =  sufAr[j] * nums[i]
                j += 1
            j = i+1 
            while j < len(nums):
                prefixAr[j] = prefixAr[j] * nums[i]
                j += 1
        for i in range(len(nums)):
            finalar.append(prefixAr[i] * sufAr[i])
        return finalar




        