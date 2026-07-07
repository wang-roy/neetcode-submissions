class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0
        left = 0
        right = n-1
        running_height = 0
        while left < right:
            left_bar = height[left]
            right_bar = height[right]
            curr_height = min(left_bar, right_bar)
            if left_bar == curr_height:
                total_water -= min(running_height, left_bar)
                left += 1
            else:
                total_water -= min(running_height, right_bar)
                right -= 1
            if curr_height > running_height:
                total_water += (curr_height - running_height) * (right-left)
                running_height = curr_height
        return total_water
            
            
