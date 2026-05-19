class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = list()
    nums.sort()
    for i in range(len(nums)):
      if nums[i] > 0:
        break
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      l = i+1
      h = len(nums) - 1
      while l < h:
        threeSum = nums[i] + nums[l] + nums[h]
        if threeSum < 0:
          l += 1
        elif threeSum > 0:
          h-=1
        else:
          result.append([nums[i],nums[l],nums[h]])
          l += 1
          h -= 1
          while nums[l] == nums[l - 1] and l < h:
            l += 1

    return result