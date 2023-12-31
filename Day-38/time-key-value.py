from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        # key -> (time, val)
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # appending will sort by timestamp
        # since timestamps are strictly increasing
        # according to the problem
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timeseries = self.map[key]
        
        if not timeseries:
            return ""
        
        # this is the potential index of the first timestamp
        # that is strictly greater than timestamp
        idx = bisect_right(timeseries, timestamp, key=lambda o:o[0])
        
        # given timestamp is smaller than anything seen
        if idx == 0:
            return ""
        
        return timeseries[idx-1][1]
        
class TimeMap:
    
    def __init__(self):
        self.store = {}
        
    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        
    def get(self, key, timestamp):
        res = ""
        values = self.store.get(key, [])
        
        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
    
        
timemap = TimeMap()
timemap.set("foo", "bar", 1)
timemap.set("foo", "bar2", 3)
timemap.get("key", 1)
