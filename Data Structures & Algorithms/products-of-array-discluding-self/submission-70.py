class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)
        result = [1] * len(nums)

        left = 1 
        for i in range(len(nums)):
            left_products[i] = left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            right_products[i] = right
            right *= nums[i]

        for i in range(len(nums)):
            result[i] = left_products[i] * right_products[i]

        return result