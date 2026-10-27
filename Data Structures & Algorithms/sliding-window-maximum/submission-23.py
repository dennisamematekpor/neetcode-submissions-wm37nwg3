class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window problem
        left = right = 0
        decreasing_deque = deque()
        result = []

        while right < len(nums):
            while decreasing_deque and nums[right] > nums[decreasing_deque[-1]]:
                decreasing_deque.pop()
            decreasing_deque.append(right)
            
            if left > decreasing_deque[0]:
                decreasing_deque.popleft()

            if (right + 1) >= k:
                result.append(nums[decreasing_deque[0]])
                left += 1

            right += 1

        return result