class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxArea = 0
        while left < right:
            containerHeight = min(heights[left], heights[right])
            area = (right - left) * containerHeight
            if area > maxArea:
                maxArea = area
            if heights[left] == containerHeight:
                left += 1
            else:
                right -= 1
        
        return maxArea
            