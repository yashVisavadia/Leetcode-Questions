from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = 0
        prev = 0
        n = 0
        print(prev, n)
        for i in gain:
            n = prev + i
            prev = n
            print(prev, n)
            maxi = max(maxi, n)
        return maxi


obj = Solution()
print(obj.largestAltitude([[-5, 1, 5, 0, -7]]))
