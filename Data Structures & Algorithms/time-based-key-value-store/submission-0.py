class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        vals = [(timestamp, value)]
        if self.timeMap.get(key):
            vals = self.timeMap[key] + [(timestamp, value)]
        self.timeMap.update({key:vals})
        print(self.timeMap)
            
    def get(self, key: str, timestamp: int) -> str:
        if not self.timeMap.get(key):
            return ""
        vals = self.timeMap[key]
        print(vals)
        left = 0
        right = len(vals)-1
        prev = None
        while left <= right:
            mid = (left + right)//2
            if vals[mid][0] < timestamp:
                prev = vals[mid][1]
                left = mid+1
            elif vals[mid][0] > timestamp:
                right = mid-1
            else:
                prev = vals[mid][1]
                break
        if prev is None:
            return ""
        return prev

