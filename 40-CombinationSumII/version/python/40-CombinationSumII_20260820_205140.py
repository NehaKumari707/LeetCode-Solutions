# Last updated: 8/20/2026, 8:51:40 PM
1class Solution(object):
2
3  def combinationSum2(self, candidates, target):
4    candidates.sort()  # Step 1: Sort to group duplicates together
5    result = []
6
7    def backtrack(start_idx, path, remaining):
8      if remaining == 0:
9        result.append(list(path))
10        return
11
12      for i in range(start_idx, len(candidates)):
13        # Early pruning: since array is sorted, larger numbers won't fit
14        if candidates[i] > remaining:
15          break
16
17        # Step 2: Skip duplicate elements at the same tree level
18        if i > start_idx and candidates[i] == candidates[i - 1]:
19          continue
20
21        path.append(candidates[i])
22        # Step 3: Recurse with `i + 1` (each element used at most once)
23        backtrack(i + 1, path, remaining - candidates[i])
24        path.pop()
25
26    backtrack(0, [], target)
27    return result