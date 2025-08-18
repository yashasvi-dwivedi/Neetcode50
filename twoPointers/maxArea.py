class Solution:
    def maxArea(self, heights):
        L, r = 0, len(heights) - 1
        res = 0

        while L < r:
            area = min(heights[L], heights[r]) * (r - L)
            res = max(res, area)
