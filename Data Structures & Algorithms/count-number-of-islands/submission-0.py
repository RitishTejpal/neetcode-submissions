class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c, visited):
            if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
                return
            if grid[r][c] == "0" or (r, c) in visited:
                return
            
            visited.add((r, c))
            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)

        visited = set()
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "0" or (r, c) in visited:
                    continue
                dfs(r, c, visited)
                islands += 1
        
        return islands