import heapq
class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        self.heap.append(num)

    def findMedian(self) -> float:
        temp = self.heap[:]
        n = len(temp)
        heapq.heapify(temp)
        if n&1:
            k = len(temp)//2
        else:
            k = len(temp)//2 - 1

        while k:
            heapq.heappop(temp)
            k-=1
        return heapq.heappop(temp)*1.0 if n&1 else (heapq.heappop(temp) + heapq.heappop(temp))/2
            