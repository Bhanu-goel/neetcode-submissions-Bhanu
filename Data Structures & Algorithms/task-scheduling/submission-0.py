from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxcount = max(freq.values())
        nummax = sum(1 for t in freq if freq[t] == maxcount)
        return max(len(tasks),(maxcount-1)*(n+1)+nummax)
