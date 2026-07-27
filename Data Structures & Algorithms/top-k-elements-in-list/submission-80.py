class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = defaultdict(list)
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for num, cnt in count.items():
            frequent[cnt].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            for num in frequent[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return []