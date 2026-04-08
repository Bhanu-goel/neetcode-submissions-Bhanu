class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        # print(count)
        freq = [[] for i in range(len(nums)+1)]
        # print(freq)
        for key,v in count.items():
            freq[v].append(key)
        # print(freq)
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res