class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        # print(freq)
        freq1=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        # print(freq1)
        res = []
        for i in freq1:
            res.append(i[0])
        return res[:k]
        