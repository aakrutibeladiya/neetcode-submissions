class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSubString = ""
        sublength = 0
        if len(s) <= 1:
            return s
        for i in range(len(s)):
            #even lenght substring
            l,r = i,i+1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                if r-l+1 > sublength:
                    sublength = r-l+1
                    longestSubString = s[l:r+1]
                r += 1
                l -= 1
            
            # odd lenght substring
            l ,r = i, i
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                if r-l+1 > sublength:
                    sublength = r-l+1
                    longestSubString = s[l:r+1]
                r += 1
                l -= 1
            
        return longestSubString     


