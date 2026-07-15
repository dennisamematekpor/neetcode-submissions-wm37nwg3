class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str 
        
    def decode(self, s: str) -> List[str]:
        start_index = 0
        result = []

        while start_index < len(s):
            pound_index = start_index

            while s[pound_index] != "#":
                pound_index += 1

            str_length = int(s[start_index : pound_index])
            start_index = pound_index + 1
            decoded_str = s[start_index : start_index + str_length]
            result.append(decoded_str)
            start_index += str_length

        return result

