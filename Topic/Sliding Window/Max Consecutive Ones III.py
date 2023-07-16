from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int):

        i = j = 0
        ones = 0
        while j < len(nums):
            if nums[j] == 0:
                ones += 1
            if ones > k:
                if nums[i] == 0:
                    ones -= 1
                i += 1
            j += 1
        return j - i


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(sol.longestOnes(nums, k))
