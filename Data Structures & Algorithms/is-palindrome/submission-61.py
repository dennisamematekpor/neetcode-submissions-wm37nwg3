class Solution:
    def isPalindrome(self, s: str) -> bool:
        # We create a left and right pointer for each and skip non alphanumeric characters
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False 
            else:
                left += 1
                right -= 1

        return True