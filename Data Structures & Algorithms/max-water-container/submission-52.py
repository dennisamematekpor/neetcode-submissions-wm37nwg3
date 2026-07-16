class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        max_area = 0
        
        left, right = 0, len(heights) - 1
        while left < right: 
            current_area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, current_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area