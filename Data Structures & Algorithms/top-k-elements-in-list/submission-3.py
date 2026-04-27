class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        htable = {}
        values = []
        if k == len(nums):
            return nums
        for num in nums:
            if num in htable:
                htable[num] += 1
            else:
                htable.update({num: 1})
        for val in htable.values():
            values.append(val)
        values = sorted(values, reverse=True)
        top_k_threshold = values[k-1]
        arr = list()
        for key, v in htable.items():
            if v >= top_k_threshold:
                arr.append(key)
        return arr