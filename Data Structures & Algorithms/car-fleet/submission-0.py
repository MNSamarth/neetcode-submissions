class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        data=[]
        count=0
        for p, s in zip(position, speed):
            data.append([p, (target-p)/s])
        data.sort(key=lambda x:x[0], reverse=True)
        for d in data:
            if stack:
                if d[1]>stack[-1][1]:
                    stack=[]
                    count+=1
                else:
                    d[1]=max(stack[-1][1],d[1])
                stack.append(d)
            else:
                stack.append(d)
        if stack:
            count+=1
        return count