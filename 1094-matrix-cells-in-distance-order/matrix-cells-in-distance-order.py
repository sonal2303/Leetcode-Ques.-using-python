class Solution:
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        cells = []

        for i in range(rows):
            for j in range(cols):
                distance = abs(i - rCenter) + abs(j - cCenter)
                cells.append((distance, [i, j]))

        cells.sort()

        return [cell[1] for cell in cells]