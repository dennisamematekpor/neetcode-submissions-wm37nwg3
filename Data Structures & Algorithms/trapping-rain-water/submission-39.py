class Solution:
    def trap(self, height: List[int]) -> int:
        water_trapped = 0
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_boundary, right_boundary = height[left], height[right]

        while left < right:
            if left_boundary < right_boundary:
                left += 1
                left_boundary = max(left_boundary, height[left])
                water_trapped += left_boundary - height[left]
            else:
                right -= 1
                right_boundary = max(right_boundary, height[right])
                water_trapped += right_boundary - height[right]
        
        return water_trapped