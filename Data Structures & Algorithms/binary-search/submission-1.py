class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        def binarySearch(left, right):
            if right == left and nums[left] == target:
                return left
            if right <= left:
                return -1
            
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return binarySearch(left, mid)
            elif target > nums[mid]:
                return binarySearch(mid + 1, right)

        return binarySearch(left, right)
