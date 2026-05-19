class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) - 1
        results = list()
        while low <= high:
            # we need to find max(min height of selected bars * distance between bars)
            results.append(min(heights[high],heights[low]) * (high-low))
            if heights[low] <= heights[high]:
                low += 1
            else:
                high -= 1

        return max(results)