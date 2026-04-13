class Solution:
    grp = list()
    ls = list()
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        htable = {}
        for str in strs:
            ordered_str = tuple(sorted(tuple(str)))
            if ordered_str not in htable:
                self.grp = []
                htable.update({ordered_str:self.grp})
            if ordered_str in htable:
                htable[ordered_str].append(str)
        self.ls.clear()
        for v in htable.values():
            self.ls.append(v)
        return self.ls

