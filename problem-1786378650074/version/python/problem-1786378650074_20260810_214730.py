# Last updated: 8/10/2026, 9:47:30 PM
1class Solution:
2    def threeSumClosest(self, nums, target):
3        nums.sort()
4
5        ans = nums[0] + nums[1] + nums[2]
6
7        for i in range(len(nums) - 2):
8            left = i + 1
9            right = len(nums) - 1
10
11            while left < right:
12                curr = nums[i] + nums[left] + nums[right]
13
14                if abs(curr - target) < abs(ans - target):
15                    ans = curr
16
17                if curr < target:
18                    left += 1
19                elif curr > target:
20                    right -= 1
21                else:
22                    return curr
23
24        return ans