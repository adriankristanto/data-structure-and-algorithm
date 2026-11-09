import math


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

        # flattening 2D index to 1D
        # in sudoku, we have the following inner boxes
        # 0 1 2
        # 3 4 5
        # 6 7 8
        # an element at index i, j belong to one of these inner boxes
        # e.g., element at index 7, 4 belong to the box at row 7 // 3 = 2, and column 4 // 3 = 1, so it belongs to the inner box number 7
        # we can flatten the boxes into 0 1 2 | 3 4 5 | 6 7 8
        # so, given row 2, we know that it belongs to one of the boxes in the last row (2 * 3) = a box in one of the indices 6 7 8. The column is 1, so (2 * 3) + 1 = 7 (so inner box number 7)
        # the general formula is row * width + column
        length = len(board)
        side = int(math.sqrt(length))
        inners = [[] for _ in range(length)]
        for i in range(length):
            for j in range(length):
                innerBoxRow = i // side
                innerBoxCol = j // side
                boxIndex = innerBoxRow * side + innerBoxCol
                inners[boxIndex].append(board[i][j])

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
