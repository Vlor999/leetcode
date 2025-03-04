#! /usr/bin/env python3

class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        left, right = 0, len(values) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res


def main():
    timeMap = TimeMap()
    timeMap.set("ctondw","ztpearaw",1)
    timeMap.set("vrobykydll","hwliiq",2)
    timeMap.set("gszaw","ztpearaw",3)
    timeMap.set("ctondw","gszaw",4)
    timeMap.get("gszaw",5)

if __name__ == "__main__":
    main()