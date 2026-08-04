class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_elements = []
        left = 0
        max_elements.append(max(nums[left : k]))
        for right in range(k, len(nums)):
            left += 1
            max_elements.append(max(nums[left : right + 1]))
        return max_elements