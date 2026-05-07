from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxcount = defaultdict(int)
        for i,v in enumerate(nums):
            maxcount[v] += 1
        sortedAr = sorted(maxcount, key=lambda x: maxcount[x], reverse=True)
        return sortedAr[:k]      