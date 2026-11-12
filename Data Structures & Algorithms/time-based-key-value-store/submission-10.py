class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        left = 0
        right = len(self.store[key]) - 1
        answer = ""

        while left <= right:
            middle = left + (right - left) // 2

            if self.store[key][middle][1] <= timestamp:
                answer = self.store[key][middle][0]
                left = middle + 1
            else:
                right = middle - 1

        return answer

        
