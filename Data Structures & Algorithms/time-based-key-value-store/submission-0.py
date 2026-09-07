class TimeMap:

    def __init__(self):
        self.lookup={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.lookup:
            self.lookup[key]=[]

        self.lookup[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.lookup:
            return ""
        items=self.lookup.get(key)
        left=0
        right=len(items)-1
        result=''
        while(left<=right):
            mid=(left+right)//2
            if items[mid][0]<=timestamp:
                result=items[mid][1]
                left=mid+1
            else:
                right=mid-1
        return result
        # for i in range(timestamp,-1,-1):
        #     k=key+'time'+str(i)
        #     if k in self.lookup:
        #         return self.lookup[k]
        # return ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)