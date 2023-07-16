from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        for i, v in enumerate(nums, 1):
            if len(nums) % i == 0:
                ans += v * v
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 4, 3, 2]
    print(sol.sumOfSquares(nums))
