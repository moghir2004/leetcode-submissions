import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.findall(r"\w+", s)).lower().strip()
        if s == "" or len(s) == 1:
            return True
        l = 0
        h = len(s) - 1
        b = False
        while h > l:
            if s[l] == s[h]:
                b = True
                h -= 1
                l += 1
            else:
                b = False
                h = 0
        return b

