class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrak(i, cur, total):

            #1st base case
            if total == target:
                res.append(cur.copy())
                return

            #2nd base case
            if i >= len(candidates) or total > target:
                return
            
            #incluse
            cur.append(candidates[i])
            backtrak(i+1, cur, total + candidates[i]) 

            #not include
            cur.pop()
            while i+ 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrak(i+1, cur, total)

        backtrak(0, [], 0)

        return res