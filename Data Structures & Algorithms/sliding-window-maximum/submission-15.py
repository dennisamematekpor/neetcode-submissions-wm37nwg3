class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        decreasing_deque = deque()
        left = right = 0

        while right < len(nums):

            # Remove from back - smaller elements can never be the maximum
            while decreasing_deque and nums[decreasing_deque[-1]] < nums[right]:
                decreasing_deque.pop()
            decreasing_deque.append(right)

            # Remove from the front - index has fallen outside the window
            # the same concept of removing elements to shrink the window
            if left > decreasing_deque[0]:
                decreasing_deque.popleft()

            # Window is fully formed - record the maximum
            if (right + 1) >= k:
                output.append(nums[decreasing_deque[0]])
                left += 1

            right += 1
        
        return output