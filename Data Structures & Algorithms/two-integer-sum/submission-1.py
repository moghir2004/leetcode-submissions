class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            hash_table.update({nums[i]:i})
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_table and hash_table[difference] != i:
                return [i, hash_table[difference]]