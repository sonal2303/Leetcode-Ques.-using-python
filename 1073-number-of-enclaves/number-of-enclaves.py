class Solution:
    def numEnclaves(self, grid):
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if grid[r][c] == 0:
                return

            grid[r][c] = 0

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Remove land connected to the top and bottom borders
        for c in range(n):
            if grid[0][c] == 1:
                dfs(0, c)

            if grid[m - 1][c] == 1:
                dfs(m - 1, c)

        # Remove land connected to the left and right borders
        for r in range(m):
            if grid[r][0] == 1:
                dfs(r, 0)

            if grid[r][n - 1] == 1:
                dfs(r, n - 1)

        # Count remaining land cells
        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    count += 1

        return count