from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int):
        nums.sort()
        i = 0
        for j in range(len(nums)):
            if nums[j] - nums[i] > 2 * k:
                i += 1
        return j - i + 1


if __name__ == "__main__":
    sol = Solution()
    nums = [10, 59, 86]
    k = 23
    print(sol.maximumBeauty(nums, k))
