class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,h = 0,len(numbers)-1
        while h > l:
            if numbers[l] + numbers[h] == target:
                return [l+1,h+1]
            elif numbers[l] + numbers[h] < target:
                l += 1
            else:
                h -= 1