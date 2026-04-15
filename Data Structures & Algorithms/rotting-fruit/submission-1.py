class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        fresh = 0
        q = []
                    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.pop(0)
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in directions:
                    x, y = r + dx, c + dy
                    if(
                        x in range(len(grid)) and y in range(len(grid[0])) and
                        grid[x][y] == 1
                    ):
                        grid[x][y] = 2
                        q.append((x, y))
                        fresh -= 1
            mins += 1

        return mins if fresh == 0 else -1