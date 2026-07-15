class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get the numbers in order by first getting the frequency of each number 
        frequency = defaultdict(list)
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for num, count in count.items():
            frequency[count].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            for val in frequency[i]:
                result.append(val)  
                if len(result) == k:
                    return result

        return []