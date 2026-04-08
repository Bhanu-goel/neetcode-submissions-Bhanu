class TimeMap:

    def __init__(self):
        self.tstmp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tstmp[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tstmp:
            return ''
        lst = self.tstmp[key]
        l = 0
        r = len(lst) - 1
        indx = -1
        while l<=r:
            mid = l + (r - l)//2
            if lst[mid][0] <= timestamp:
                indx = mid
                l = mid+1
            else:
                r = mid - 1
        # print(indx)
        return lst[indx][1] if indx != -1 else ''