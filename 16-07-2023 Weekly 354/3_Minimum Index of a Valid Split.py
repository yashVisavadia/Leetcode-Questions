from collections import Counter
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]):
        major, cnt = Counter(nums).most_common()[0]

        l, r = 0, cnt
        n = len(nums)
        for i in range(n):
            if nums[i] == major:
                l += 1
                r -= 1

            if 2 * l > i + 1 and 2 * r > n - i - 1:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 3, 3, 3, 7, 2, 2]
    print(sol.minimumIndex(nums))
    pass
