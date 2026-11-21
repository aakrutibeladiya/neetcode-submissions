class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        if len(s) <= 1:
            return 1
        for i in range(len(s)):
            #even lenght substring
            l,r = i,i+1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                count += 1
                r += 1
                l -= 1
            
            # odd lenght substring
            l ,r = i, i
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                count += 1
                r += 1
                l -= 1
            
        return count   


