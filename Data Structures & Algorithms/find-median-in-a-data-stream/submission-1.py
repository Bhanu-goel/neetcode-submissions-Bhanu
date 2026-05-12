class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr)&1:
            n1 = self.arr[len(self.arr)//2]
            return n1*1.0
        else:
            n1 = self.arr[len(self.arr)//2]
            n2 = self.arr[len(self.arr)//2-1]
            return (n1+n2)/2