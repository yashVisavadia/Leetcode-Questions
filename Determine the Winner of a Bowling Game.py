from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(nums):
            arr = [0, 0] + nums
            ans = 0
            for i in range(2, len(arr)):
                if arr[i - 1] == 10 or arr[i-2] == 10:
                    ans += 2 * arr[i]
                else:
                    ans += arr[i]
            return ans

        s1 = score(player1)
        s2 = score(player2)

        if s1 == s2:
            return 0
        elif s1 > s2:
            return 1
        return 2
