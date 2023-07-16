import bisect
from sortedcontainers import SortedList
from typing import List


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:

        for i in range(len(nums)):
            nums[i] = min(0, nums[i])

        ans = []
        s = SortedList(nums[:k])

        ans.append(s[x-1])
        for i in range(k, len(nums)):
            s.remove(nums[i - k])
            # bisect.insort(s, nums[i])
            s.add(nums[i])
            # print('s --- ', s)
            ans.append(s[x-1])

        return ans


obj = Solution()
print(obj.getSubarrayBeauty([-3, 1, 2, -3, 0, -3], 2, 1))
