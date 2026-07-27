class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for pivot_index, pivot in enumerate(nums):
            if pivot > 0:
                break
            
            if pivot_index > 0 and nums[pivot_index] == nums[pivot_index - 1]:
                continue 

            left, right = pivot_index + 1, len(nums) - 1
            while left < right:
                current_sum = pivot + nums[left] + nums[right]
                if current_sum == 0:
                    triplets.append([pivot, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1

        return triplets