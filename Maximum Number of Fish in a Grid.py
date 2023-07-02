from typing import List
from sys import maxsize


class Solution:
    temp = 0

    def findMaxFish(self, grid: List[List[int]]) -> int:
        flags = [[0 for j in range(len(grid[i]))] for i in range(len(grid))]

        def helper(i, j):
            if grid[i][j] == 0 or flags[i][j]:
                return Solution.temp

            u = d = l = r = 0
            flags[i][j] = True
            Solution.temp += grid[i][j]
            if i - 1 >= 0 and grid[i - 1][j] != 0 and not flags[i - 1][j]:
                helper(i - 1, j)
            if i + 1 < len(grid) and grid[i + 1][j] != 0 and not flags[i + 1][j]:
                helper(i + 1, j)
            if j - 1 >= 0 and grid[i][j - 1] != 0 and not flags[i][j - 1]:
                helper(i, j - 1)
            if j + 1 < len(grid[i]) and grid[i][j + 1] != 0 and not flags[i][j + 1]:
                helper(i, j + 1)

            # if grid[i][j] == 0 or flags[i][j]:
            #     return cnt
            # u = d = l = r = 0

            # flags[i][j] = 1
            # flag = False
            # if i - 1 >= 0 and grid[i - 1][j] != 0 and not flags[i - 1][j]:
            #     u = helper(i - 1, j, cnt + grid[i][j])
            #     flag = True
            # if i + 1 < len(grid) and grid[i + 1][j] != 0 and not flags[i + 1][j]:
            #     d = helper(i + 1, j, cnt + grid[i][j])
            #     flag = True
            # if j - 1 >= 0 and grid[i][j - 1] != 0 and not flags[i][j - 1]:
            #     l = helper(i, j - 1, cnt + grid[i][j])
            #     flag = True
            # if j + 1 < len(grid[i]) and grid[i][j + 1] != 0 and not flags[i][j + 1]:
            #     r = helper(i, j + 1, cnt + grid[i][j])
            #     flag = True
            # if not flag:
            #     u += cnt + grid[i][j]

            # return u + d + l + r

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0 and not flags[i][j]:
                    Solution.temp = 0
                    helper(i, j)
                    ans = max(ans, Solution.temp)
        return ans


obj = Solution()
grid = [[10, 5], [8, 0]]
print(obj.findMaxFish(grid))
