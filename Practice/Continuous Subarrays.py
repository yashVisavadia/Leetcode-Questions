from typing import List
from sortedcontainers import SortedList


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        sli = SortedList()
        ans = 0
        l = 0
        for r, x in enumerate(nums):
            sli.add(x)
            while sli[-1] - sli[0] > 2:
                sli.remove(nums[l])
                l += 1
            ans += r - l + 1
        return ans


obj = Solution()
print(obj.continuousSubarrays([5, 4, 2, 4]))
