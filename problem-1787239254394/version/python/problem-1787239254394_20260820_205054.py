# Last updated: 8/20/2026, 8:50:54 PM
1class Solution(object):
2
3  def combinationSum(self, candidates, target):
4    result = []
5
6    def backtrack(start_idx, path, remaining):
7      if remaining == 0:
8        result.append(list(path))
9        return
10
11      for i in range(start_idx, len(candidates)):
12        coin = candidates[i]
13        if coin > remaining:
14          continue
15
16        path.append(coin)
17        backtrack(i, path, remaining - coin)
18        path.pop()
19
20    backtrack(0, [], target)
21    return result