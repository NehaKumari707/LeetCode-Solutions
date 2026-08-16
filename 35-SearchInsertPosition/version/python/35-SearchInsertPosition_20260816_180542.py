# Last updated: 8/16/2026, 6:05:42 PM
1class Solution:
2    def searchInsert(self, nums, target):
3        left = 0
4        right = len(nums) - 1
5
6        while left <= right:
7            mid = (left + right) // 2
8
9            if nums[mid] == target:
10                return mid
11
12            elif nums[mid] < target:
13                left = mid + 1
14
15            else:
16                right = mid - 1
17
18        return left