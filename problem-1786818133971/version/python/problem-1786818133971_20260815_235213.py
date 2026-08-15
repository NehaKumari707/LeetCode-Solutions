# Last updated: 8/15/2026, 11:52:13 PM
1class Solution(object):
2    def nextPermutation(self, nums):
3        n = len(nums)
4        i = n - 2
5
6        while i >= 0 and nums[i] >= nums[i + 1]:
7            i -= 1
8
9        if i >= 0:
10            j = n - 1
11
12            while nums[j] <= nums[i]:
13                j -= 1
14
15            nums[i], nums[j] = nums[j], nums[i]
16
17        left = i + 1
18        right = n - 1
19
20        while left < right:
21            nums[left], nums[right] = nums[right], nums[left]
22            left += 1
23            right -= 1