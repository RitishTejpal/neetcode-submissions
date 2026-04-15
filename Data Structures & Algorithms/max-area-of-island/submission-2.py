class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            nonlocal maxArea, visited
            if (
                not 0 <= r < len(grid) or
                not 0 <= c < len(grid[0]) or
                (r, c) in visited or
                grid[r][c] == 0
            ):
                return 0
            
            visited.add((r, c))

            return (1 + dfs(r + 1, c) +
            dfs(r - 1, c) +
            dfs(r, c + 1) +
            dfs(r, c - 1))
        
        maxArea = 0
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                maxArea = max(maxArea, dfs(r, c))
        
        return maxArea
