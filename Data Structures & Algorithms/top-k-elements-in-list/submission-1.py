class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a hashmap to keep count of the frequency of each number
        # have a max_frequency array to keep the numbers with the max frequencys

        #loop through nums once and keep count of the max and the frequencies

        #Bucket sort?
        buckets = [[] for _ in range(len(nums) + 1)]

        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1

        for freq in frequencies:
            buckets[frequencies[freq]].append(freq)

        top_freq = []

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
            