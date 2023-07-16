from typing import List


class Solution:

    def maximumJumps(self, nums: List[int], t: int) -> int:
        def rec(st, ret):
            if st == len(nums) - 1:
                return ret

            r = 0
            for end in range(st + 1, len(nums)):
                if abs(nums[st] - nums[end]) <= t:
                    p = rec(end, ret + 1)
                    r = max(p, r)
                    if p == -1:
                        r = -1
            if r == 0 or r == -1:
                return -1
            return r

        i, j = 0, 1
        cnt = 0
        ans = 0
        while j != len(nums):
            if abs(nums[i] - nums[j]) <= t:
                temp = rec(j, cnt + 1)
                ans = max(ans, temp)
            j += 1

        if ans == 0 or ans == -1:
            return -1
        return ans


obj = Solution()
print(obj.maximumJumps([0, 2, 3, 1, 4], 2))
