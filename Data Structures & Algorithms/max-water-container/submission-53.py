class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        if not heights:
            return 0

        left, right = 0, len(heights) - 1

        while left < right:
            width = right - left 
            current_area = min(heights[left], heights[right]) * width 
            max_area = max(max_area, current_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area