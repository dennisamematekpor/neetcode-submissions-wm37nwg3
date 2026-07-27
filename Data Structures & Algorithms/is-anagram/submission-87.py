class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # We check for the length first
        if len(s) != len(t):
            return False 
        
        # For an anagram, they should both contain the same characters (equal length, same characters)
        char_count = [0] * 26
        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1
            char_count[ord(t[i]) - ord('a')] -= 1

        for val in char_count:
            if val != 0:
                return False 
            
        return True