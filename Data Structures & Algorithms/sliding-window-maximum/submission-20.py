class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we need a sliding window and the data structure for this is a double ended queue
        # since it is a fixed k sliding window, we need a left and a right plus a condition
        # to keep the window at k with every shift in right and left
        # the double ended queue allows O(1) insertion and removal of elements

        left = right = 0
        decreasing_deque = deque()
        result = []

        while right < len(nums):
            # we want to loop through all the values once
            while decreasing_deque and nums[right] > nums[decreasing_deque[-1]]:
                # while the deque exists and the number in the nums is greater than the 
                # the last number in the decreasing deque(the last number is small value)
                # since the deque is meant to save numbers decreasing
                # note the deque only saves indices not values
                decreasing_deque.pop() # remove indices from the right
            decreasing_deque.append(right)
            # after popping all the smaller values, we now append the max value 
            # in the decreasing deque(we append the index not the value itself)

            if(right + 1) >= k:
                # if we obtain the window k, move the left pointer and store the max value
                # in the result array
                result.append(nums[decreasing_deque[0]])
                # the max value would be at the front of the deque
                left += 1 # move the left pointer forward
            
            # after moving the left index, the valid window would be out of context in the 
            # deque
            if left > decreasing_deque[0]:
                decreasing_deque.popleft() # remove indices from the front

            # since it is a while loop, we move the right index manually
            right += 1

        return result # return the values of the max elements