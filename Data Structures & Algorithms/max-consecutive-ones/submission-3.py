class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count +=1
                maxcount = max(count, maxcount)
            else:
                count = 0
        return maxcount
        