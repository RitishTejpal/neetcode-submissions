class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == ".":
                    continue
                if curr in rows[r]: 
                    return False
                else:
                    rows[r].add(curr)

                if curr in cols[c]: 
                    return False
                else:
                    cols[c].add(curr)

                if curr in grid[(r // 3, c // 3)]: 
                    return False
                else:
                    grid[(r // 3, c // 3)].add(curr)
        
        return True

                
