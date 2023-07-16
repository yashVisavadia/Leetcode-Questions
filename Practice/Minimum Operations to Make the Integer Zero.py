class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(61):
            target = num1 - k * num2
            if target >= 0 and target.bit_count() <= k <= target:
                return k
        return -1


obj = Solution()
print(obj.makeTheIntegerZero(5, -21))
