class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup=set(nums)
        return False if len(nums)==len(lookup) else True
