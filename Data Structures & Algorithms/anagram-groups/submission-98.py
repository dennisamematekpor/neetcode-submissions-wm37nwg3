class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # in a dictionary, make a hash tuple for each word in the string
        # append similar characters to the same list using two loops
        # one for the word and the next for the characters
        group = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            group[tuple(char_count)].append(word)
        return list(group.values())