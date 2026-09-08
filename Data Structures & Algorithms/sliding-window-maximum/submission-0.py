from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        max_window=[]
        q=deque()
        for right in range(len(nums)):
            while(q and nums[right]>=nums[q[-1]]):
                q.pop()
            q.append(right)
            if right-left+1==k:
                max_window.append(nums[q[0]])
                if left==q[0]:
                    q.popleft()
                left+=1
        return max_window

