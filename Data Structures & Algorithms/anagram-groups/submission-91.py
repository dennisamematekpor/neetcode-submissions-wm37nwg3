class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We want to group the words with a key
        group_anagram = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            group_anagram[tuple(char_count)].append(word)
        return list(group_anagram.values())