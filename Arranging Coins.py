class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = (l + r + 1) >> 1
            if (mid * (mid + 1)) // 2 <= n:
                l = mid
            else:
                r = mid - 1
        return l


obj = Solution()
print(obj.arrangeCoins(5))
