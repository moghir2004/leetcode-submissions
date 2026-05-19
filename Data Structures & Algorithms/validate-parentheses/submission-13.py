class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        opening_to_closing = {
            ')':'(',
            '}':'{',
            ']':'['
            }
        for i in range(len(s)):
            if s[i] in opening_to_closing:
                if stack and stack[-1] == opening_to_closing[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False
