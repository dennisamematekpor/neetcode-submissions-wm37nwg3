class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        most_freq = 0
        left = 0
        longest = 0

        for right in range(len(s)):
            char_count[s[right]] += 1
            most_freq = max(most_freq, char_count[s[right]])
            # the window 
            while right - left + 1 - most_freq > k:
                char_count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
            