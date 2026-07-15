class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We want to add two items for a sum
        # If we take a number from a target we get a compliment

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num 
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        # we are working with their indexes
        return []