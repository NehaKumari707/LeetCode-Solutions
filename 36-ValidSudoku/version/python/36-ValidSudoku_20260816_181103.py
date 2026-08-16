# Last updated: 8/16/2026, 6:11:03 PM
1class Solution:
2    def isValidSudoku(self, board):
3        rows = [set() for _ in range(9)]
4        cols = [set() for _ in range(9)]
5        boxes = [set() for _ in range(9)]
6
7        for r in range(9):
8            for c in range(9):
9
10                if board[r][c] == ".":
11                    continue
12
13                num = board[r][c]
14
15                # Row check
16                if num in rows[r]:
17                    return False
18                rows[r].add(num)
19
20                # Column check
21                if num in cols[c]:
22                    return False
23                cols[c].add(num)
24
25                # 3x3 box check
26                box = (r // 3) * 3 + (c // 3)
27
28                if num in boxes[box]:
29                    return False
30                boxes[box].add(num)
31
32        return True