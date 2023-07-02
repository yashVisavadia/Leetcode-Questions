from typing import List


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        ans, m = 1, 10 ** 9 + 7
        cnt = i = 0

        while i < len(nums) and nums[i] == 0:
            i += 1

        if i == len(nums):
            return 0

        while i < len(nums):
            if nums[i] == 1:
                ans = (ans * (cnt + 1)) % m
                cnt = 0
            else:
                cnt += 1
            i += 1
        return ans


obj = Solution()
print(obj.numberOfGoodSubarraySplits([0, 0]))
