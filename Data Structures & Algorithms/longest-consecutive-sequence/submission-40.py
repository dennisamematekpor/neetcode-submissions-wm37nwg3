class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if (num - 1) not in num_set:
                current_len = 0
                while num + current_len in num_set:
                    current_len += 1
                longest = max(longest, current_len)
        return longest