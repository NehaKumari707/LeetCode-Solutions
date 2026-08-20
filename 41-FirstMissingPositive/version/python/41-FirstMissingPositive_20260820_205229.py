# Last updated: 8/20/2026, 8:52:29 PM
1class Solution(object):
2
3  def firstMissingPositive(self, nums):
4    n = len(nums)
5
6    # Step 1: Cyclic sort - place each number x at index x - 1
7    for i in range(n):
8      while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
9        # Swap nums[i] with the number at its target index
10        target_idx = nums[i] - 1
11        nums[i], nums[target_idx] = nums[target_idx], nums[i]
12
13    # Step 2: Find the first index where nums[i] != i + 1
14    for i in range(n):
15      if nums[i] != i + 1:
16        return i + 1
17
18    # Step 3: If all numbers 1..n are present, return n + 1
19    return n + 1
20        