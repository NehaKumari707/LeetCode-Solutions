# Last updated: 8/16/2026, 6:03:47 PM
1class Solution:
2    def searchRange(self, nums, target):
3
4        def first_position():
5            left = 0
6            right = len(nums) - 1
7            ans = -1
8
9            while left <= right:
10                mid = (left + right) // 2
11
12                if nums[mid] == target:
13                    ans = mid
14                    right = mid - 1
15                elif nums[mid] < target:
16                    left = mid + 1
17                else:
18                    right = mid - 1
19
20            return ans
21
22        def last_position():
23            left = 0
24            right = len(nums) - 1
25            ans = -1
26
27            while left <= right:
28                mid = (left + right) // 2
29
30                if nums[mid] == target:
31                    ans = mid
32                    left = mid + 1
33                elif nums[mid] < target:
34                    left = mid + 1
35                else:
36                    right = mid - 1
37
38            return ans
39
40        return [first_position(), last_position()]