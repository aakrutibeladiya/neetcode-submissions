class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCounter = 0
        for i, a in enumerate(s):
            counter = 0
            uniqeString = set()
            for j in range(i, len(s)):
                if s[j] not in uniqeString:
                    counter += 1
                    maxCounter = max(maxCounter, counter)
                    uniqeString.add(s[j])
                else:
                    break
        return maxCounter   

