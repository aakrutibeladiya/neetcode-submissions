class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {},{}
        if len(s) != len(t):
            return False
        for char in range(len(s)):
            countS[s[char]] = 1 + countS.get(s[char],0)
            countT[t[char]] = 1 + countT.get(t[char],0)
        for char in countS:
            if countS[char] != countT.get(char,0):
                return False
        return True

     