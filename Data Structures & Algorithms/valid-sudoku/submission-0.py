from collections import defaultdict
from typing import List


class Solution:

  def isValidSudoku(self, board: List[List[str]]) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)

    for rowindex, row in enumerate(board):
      for colindex, cell in enumerate(row):
        if cell == ".":
          continue

        if (
            cell in rows[rowindex]
            or cell in cols[colindex]
            or cell in squares[(rowindex // 3, colindex // 3)]
        ):
          return False

        rows[rowindex].add(cell)
        cols[colindex].add(cell)
        squares[(rowindex // 3, colindex // 3)].add(cell)

    return True

