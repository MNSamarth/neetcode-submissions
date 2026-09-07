class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        if len(nums)==1:
            return nums[0]
        while(left<=right):
            if nums[left]<=nums[right]:
                return nums[left]
            else:
                left=left+1