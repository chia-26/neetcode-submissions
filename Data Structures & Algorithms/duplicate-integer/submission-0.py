class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set(nums)
        if len(nums) == len(sett):
            return False
        return True
         