class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hd = {}
        for i in strs:
            key=''.join(sorted(i))
            # print(key)
            hd.setdefault(key,[]).append(i)
        return list(hd.values())