class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())

        for i, (start, end) in enumerate(zip(s, reversed(s))):
            if i >= len(s)//2:
                break
            if start != end:
                return False
        return True