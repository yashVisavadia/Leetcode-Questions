from typing import List


class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)

        l, r = 0, n - 1

        ans = 0
        while l <= r:
            ans = max(ans, (r - l) * min(h[l], h[r]))
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return ans
