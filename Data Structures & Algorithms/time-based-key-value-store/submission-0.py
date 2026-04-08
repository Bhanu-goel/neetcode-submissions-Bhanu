class TimeMap:

    def __init__(self):
        self.tstmp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tstmp[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tstmp:
            return ''
        lst = self.tstmp[key]
        for i in range(len(lst)-1,-1,-1):
            if lst[i][0] > timestamp:
                continue
            else:
                return lst[i][1]
        return ''