from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = cnt = ans = 0
        for j in range(len(nums)):
            if nums[j] & 1:
                k -= 1
                cnt = 0
            while k == 0:
                k += nums[i] & 1
                i += 1
                cnt += 1
            ans += cnt
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k = 2
    print(sol.numberOfSubarrays(nums, k))


'''
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = j = 0
        ans = 0
        cnt = 0
        ind = []
        l = 0
        while j < len(nums):
            if nums[j] & 1 == 1:
                cnt += 1
                ind.append(j)

            while cnt > k:
                if nums[i] & 1 == 1:
                    cnt -= 1
                    l += 1
                # ans += 1
                i += 1
                # print(ans)

            if cnt == k:
                if l > 0:
                    ans += ind[l] - ind[l - 1]
                else:
                    ans += ind[l] + 1
                # print(ans)
            j += 1
        # print(ind, cnt)
        return ans
'''
