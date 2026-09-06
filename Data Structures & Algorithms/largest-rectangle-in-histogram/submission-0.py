class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        i=0
        for i in range(len(heights)):
            h=heights[i]
            if stack:
                if h<stack[-1][1]:
                    prev=[]
                    while stack and h<stack[-1][1]:
                        prev=stack.pop()
                        max_area=max((i-prev[0])*prev[1],max_area)
                    stack.append([prev[0],h])
                else:
                    stack.append([i,h])
            else:
                stack.append([i, h])
        l=len(heights)
        while(stack):
            prev=stack.pop()
            max_area=max((l-prev[0])*prev[1],max_area)
        return max_area