class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        if strs is None or len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[0][j] != strs[i][j]:
                    return prefix
            prefix += strs[0][j]
        return prefix