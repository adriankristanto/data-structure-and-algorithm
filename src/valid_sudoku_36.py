import math


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        length = len(board)
        side = int(math.sqrt(length))

        rows = [set() for _ in range(length)]
        columns = [set() for _ in range(length)]
        inners = [set() for _ in range(length)]

        for i in range(length):
            for j in range(length):
                element = board[i][j]

                # if the element is in either one of the lists, then there is a duplicate, so the board is invalid
                if element != "." and (
                    element in rows[i]
                    or element in columns[j]
                    # flatten 2d index to 1d
                    # given
                    # 0 1 2
                    # 3 4 5
                    # 6 7 8
                    # we can flatten this into
                    # 0 1 2 | 3 4 5 | 6 7 8
                    # given the coordinate (7, 4)
                    # it belongs to the inner box at row 7 // 3 = 2
                    # and column 4 // 3 = 1, i.e., (2, 1), which is box 7
                    # in 1D indexing, we can do row * width + column, so
                    # 2 * 3 + 1 = 7 (the row must start with 6, so either 6 7 8), then column 1 means we are adding 1 to the row, so we get 7
                    or element in inners[(i // side) * side + (j // side)]
                ):
                    return False

                # add the element into each of the lists
                rows[i].add(element)
                columns[j].add(element)
                inners[(i // side) * side + (j // side)].add(element)
        return True


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.isValidSudoku(
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
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
