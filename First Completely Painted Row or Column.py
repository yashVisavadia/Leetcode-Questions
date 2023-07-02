from collections import defaultdict
from sys import maxsize
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        dic = {}

        for row in range(len(mat)):
            for col in range(len(mat[row])):
                dic[mat[row][col]] = (row, col)

        for i in range(len(arr)):
            row, col = dic[arr[i]]

            rows[row] += 1
            cols[col] += 1

            if rows[row] == len(mat[row]) or cols[col] == len(mat):
                return i
        return i


obj = Solution()
arr = [5, 15, 7, 3, 4, 12, 6, 1, 8, 10, 13, 9, 2, 11, 16, 14]
mat = [[7, 12, 4, 2], [13, 5, 11, 6], [1, 14, 10, 8], [9, 16, 15, 3]]
print(obj.firstCompleteIndex(arr, mat))


# class Solution:
#     def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
#         row = len(mat)
#         col = len(mat[0])

#         dp = [0] * (row * col + 1)
#         for i, n in enumerate(arr):
#             dp[n] = i

#         ans = maxsize
#         for i in range(row):
#             s = 0
#             maxi = 0
#             for j in range(col):
#                 maxi = max(maxi, dp[mat[i][j]])
#             if ans > maxi:
#                 ans = min(maxi, ans)

#         for i in range(col):
#             s = 0
#             maxi = 0
#             for j in range(row):
#                 s += dp[mat[j][i]]
#                 maxi = max(maxi, dp[mat[j][i]])

#             if ans > maxi:
#                 ans = min(maxi, ans)

#         return ans
