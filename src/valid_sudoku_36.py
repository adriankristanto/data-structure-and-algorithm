class Solution:
    def containsDuplicate(self, lst: list[str]) -> bool:
        return len(lst) != len(set(lst))

    # remove empty entries from the list (row or column)
    def cleanup(self, lst: list[str]) -> list[str]:
        return [elem for elem in lst if elem != "."]

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            if self.containsDuplicate(self.cleanup(row)):
                return False

        # given [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        # *board will spread the array, resulting in [1, 2, 3], [4, 5, 6], [7, 8, 9]
        # then, pass into zip, resulting in zip(1, 4, 7), zip(2, 5, 8), zip(3, 6, 9), so we get
        # [[1, 4, 7], [2, 5, 8], [3, 6, 9]], the transpose of the input list
        for col in zip(*board):
            if self.containsDuplicate(self.cleanup(list(col))):
                return False

        inners = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                topLeftX, topLeftY = (i, j)
                bottomRightX, bottomRightY = (i + 2, j + 2)
                inner = []
                for x in range(topLeftX, bottomRightX + 1):
                    for y in range(topLeftY, bottomRightY + 1):
                        inner.append(board[x][y])
                inners.append(inner)

        for inner in inners:
            if self.containsDuplicate(self.cleanup(inner)):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.isValidSudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )
