class Solution:
    def projectionArea(self, grid):
        n = len(grid)
        area = 0

        for i in range(n):
            area += max(grid[i])

            area += max(grid[j][i] for j in range(n))

            for j in range(n):
                if grid[i][j] > 0:
                    area += 1

        return area