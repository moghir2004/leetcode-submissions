class Solution:
    def mySqrt(self, x: int):
        count = 0
        n = 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        while x > 0:
                x -= n
                n += 2         
                count += 1
        if x < 0:
            return count - 1
        return count