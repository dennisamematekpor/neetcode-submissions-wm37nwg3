class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        most_frequent = 0
        left = 0
        longest_str = 0

        for right in range(len(s)):
            char_count[s[right]] += 1
            most_frequent = max(most_frequent, char_count[s[right]])

            while right - left + 1 > most_frequent + k:
                char_count[s[left]] -= 1
                left += 1

            longest_str = max(longest_str, right - left + 1)

        return longest_str
            