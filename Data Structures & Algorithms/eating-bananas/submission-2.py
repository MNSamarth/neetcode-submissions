import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse=True)
        high=piles[0]
        low=1
        # lookup=set()
        min_k=high+1
        while(low<=high):
            mid=int((high+low)/2)
            hrs=0
            for p in piles:
                hrs+=math.ceil(p/mid)
            # print(hrs)
            # print(mid)
            # lookup.add(mid)
            if hrs<=h:
                min_k=min(min_k,mid)
                high=mid-1
            else:
                low=mid+1
        # return max(lookup)
        return min_k
