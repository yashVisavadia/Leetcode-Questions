from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        def common(ind):
            ans = 0
            for i in range(ind + 1):
                for j in range(ind + 1):
                    if A[i] == B[j]:
                        ans += 1
            return ans

        f1 = [0] * 51
        f2 = [0] * 51

        c = []
        for i in range(len(A)):
            f1[A[i]] += 1
            f2[B[i]] += 1

            c.append(common(i))
        return c
