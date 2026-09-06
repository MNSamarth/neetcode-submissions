from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counter counts frequencies in O(N)
        count = Counter(nums)
        
        # nlargest uses a min-heap internally to find the top k elements
        return heapq.nlargest(k, count.keys(), key=count.get)