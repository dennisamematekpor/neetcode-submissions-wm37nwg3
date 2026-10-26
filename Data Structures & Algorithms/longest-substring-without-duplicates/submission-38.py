class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        left = 0
        longest_str = 0

        for right in range(len(s)):
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1

            unique_chars.add(s[right])
            longest_str = max(longest_str, len(unique_chars))
        
        return longest_str