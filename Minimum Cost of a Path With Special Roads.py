from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from sys import maxsize
from typing import List


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        def d(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        start = tuple(start)
        target = tuple(target)

        distances = defaultdict(lambda: inf)
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            cur_dis, cur_node = heappop(pq)
            x, y = cur_node

            if (x, y) == target:
                return cur_dis

            dist = cur_dis + d((x, y), target)
            if dist < distances[target]:
                distances[target] = dist
                heappush(pq, (dist, target))

            for st_x, st_y, end_x, end_y, cost in specialRoads:
                dist = cur_dis + d((x, y), (st_x, st_y)) + cost
                if dist < distances[(end_x, end_y)]:
                    distances[end_x, end_y] = dist
                    heappush(pq, (dist, (end_x, end_y)))
        return -1


obj = Solution()
start = [1, 1]
target = [10, 9]
specialRoads = [[5, 2, 3, 6, 3], [5, 6, 9, 5, 3],
                [5, 9, 1, 2, 5], [8, 6, 9, 8, 1]]
print(obj.minimumCost(start=start, target=target, specialRoads=specialRoads))
