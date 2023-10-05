class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage.keys():
            self.storage[key] = {
                timestamp: value
            }
            return None
        
        self.storage[key][timestamp] = value
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage.keys():
            return ""
        
        if timestamp in self.storage[key].keys():
            return self.storage[key][timestamp]
        
        curr_timestamp = timestamp-1
        while curr_timestamp:
            if timestamp in self.storage[key].keys():
                return self.storage[key][timestamp]
            curr_timestamp -= 1
            
        return ""
        
        
        
timemap = TimeMap()
timemap.set("foo", "bar", 1)
timemap.set("foo", "bar2", 3)
timemap.get("key", 1)
