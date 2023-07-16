from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]):
        i = 0
        cnt = 0
        for j in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            if cnt > 1:
                if nums[i] == 0:
                    cnt -= 1
                i += 1
        return j - i


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 0, 1]
    print(sol.longestSubarray(nums))
