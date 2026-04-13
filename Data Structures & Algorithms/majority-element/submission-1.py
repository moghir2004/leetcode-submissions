class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        count = 1
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else : hmap[nums[i]] = count
        for k in hmap:
            if  len(nums)//2 < hmap[k]:
                return k
        return 0