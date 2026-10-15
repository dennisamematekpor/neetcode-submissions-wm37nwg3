class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we want the most frequent elements within the given arrays
        # we need to count the frequency of each element first with a counter
        # we need to arrange them in an order

        if k > len(nums):
            return []

        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        freq = defaultdict(list)

        for num, count in counter.items():
            freq[count].append(num)

        result = []

        for i in range(len(nums), 0, -1):
            for val in freq[i]:
                result.append(val)
                if len(result) == k:
                    return result

        return []
        