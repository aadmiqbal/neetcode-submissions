class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        wp = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[wp] = nums[i]
                wp += 1
        return wp


        