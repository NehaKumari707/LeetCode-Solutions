# Last updated: 8/10/2026, 12:07:08 AM
1class Solution:
2    def threeSum(self, nums):
3        nums.sort()
4        ans = []
5
6        for i in range(len(nums) - 2):
7
8            # Skip duplicate first numbers
9            if i > 0 and nums[i] == nums[i - 1]:
10                continue
11
12            left = i + 1
13            right = len(nums) - 1
14
15            while left < right:
16
17                total = nums[i] + nums[left] + nums[right]
18
19                if total == 0:
20                    ans.append([nums[i], nums[left], nums[right]])
21
22                    left += 1
23                    right -= 1
24
25                    # Skip duplicates
26                    while left < right and nums[left] == nums[left - 1]:
27                        left += 1
28
29                    while left < right and nums[right] == nums[right + 1]:
30                        right -= 1
31
32                elif total < 0:
33                    left += 1
34
35                else:
36                    right -= 1
37
38        return ans