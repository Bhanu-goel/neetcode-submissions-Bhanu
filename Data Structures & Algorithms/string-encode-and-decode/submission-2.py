class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(s)
            res += '!#'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        res = s.split('!#')
        res.pop()
        return res
