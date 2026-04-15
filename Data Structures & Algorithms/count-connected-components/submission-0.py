class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        ans = 0

        def bfs(node):
            q = deque([node])

            while q:
                visited[node] = True
                curr = q.popleft()
                for nei in adjlist[curr]:
                    if not visited[nei]:
                        q.append(nei)
                        visited[nei] = True
        
        for node in range(n):
            if not visited[node]:
                bfs(node)
                ans += 1
        
        return ans