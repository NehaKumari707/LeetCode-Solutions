# Last updated: 8/21/2026, 10:20:00 PM
1class Solution:
2    def trap(self, height):
3        left = 0
4        right = len(height) - 1
5
6        leftMax = 0
7        rightMax = 0
8
9        water = 0
10
11        while left < right:
12
13            if height[left] <= height[right]:
14
15                if height[left] >= leftMax:
16                    leftMax = height[left]
17                else:
18                    water += leftMax - height[left]
19
20                left += 1
21
22            else:
23
24                if height[right] >= rightMax:
25                    rightMax = height[right]
26                else:
27                    water += rightMax - height[right]
28
29                right -= 1
30
31        return water