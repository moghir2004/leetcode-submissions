class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        htable = {}
        for i in range(len(nums)):
            htable[i] = nums[i]
        if len(htable.values()) == len(set(htable.values())):
            return False
        else:
            return True