from typing import List


class Solution:
    def dfs(self, adj, v, from_node):
        ans = 0
        v[from_node] = True
        for to_node in adj[from_node]:
            if not v[abs(to_node)]:
                ans += self.dfs(adj, v, abs(to_node))
                ans += 1 if to_node > 0 else 0
        return ans

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(-u)

        v = [False] * n

        return self.dfs(adj, v, 0)
