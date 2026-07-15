class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # We want to store the characters and compare which characters are present
        # If it is present +1 if not -1
        # Let's compare their lengths first 

        if len(s) != len(t):
            return False 

        char_count = [0] * 26 
        # if char count is just zeros after running through, we got what we want
        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1
            char_count[ord(t[i]) - ord('a')] -= 1

        for val in char_count:
            if val != 0:
                return False 

        return True