class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        for start ,end in zip(s, reversed(s)):
                if start != end:
                    return False
        return True