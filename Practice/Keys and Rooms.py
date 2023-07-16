from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        v = [False] * len(rooms)
        v[0] = True

        def dfs(k):
            for i in rooms[k]:
                if not v[i]:
                    v[i] = True
                    dfs(i)

        dfs(0)
        return all(v)
