from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], t: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                for j in range(i, len(nums)):
                    if (nums[j] - nums[i] - j - i) % 2 == 0 and nums[j] <= t:
                        ans = max(ans, j - i + 1)
                    else:
                        break
        return ans

        # l = r = 0

        # while l < len(nums) and (nums[l] % 2 != 0 or nums[l] > t):
        #     l += 1

        # if l == len(nums):
        #     return 0

        # ans = 1
        # r = l + 1
        # while r < len(nums):
        #     if nums[l] % 2 == 0:
        #         if nums[r] % 2 != nums[r - 1] % 2 and (nums[r] <= t and nums[r - 1] <= t):
        #             r += 1
        #         else:
        #             ans = max(r - l, ans)
        #             l = r
        #             r += 1
        #     else:
        #         l = r
        #         r += 1

        # print(l, r)

        # return max(ans, r - l)


obj = Solution()
print(obj.longestAlternatingSubarray([8, 10, 7, 8, 3], 9))
