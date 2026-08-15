# Last updated: 8/15/2026, 11:51:05 PM
1class Solution(object):
2    def removeElement(self, nums, val):
3        k = 0
4
5        for i in range(len(nums)):
6            if nums[i] != val:
7                nums[k] = nums[i]
8                k += 1
9
10        return k
11        