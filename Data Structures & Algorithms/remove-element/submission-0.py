class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        readpointer = 0
        writepointer = 0
        for i in range(len(nums)):
            if nums[i] == val:
                readpointer +=1
            else:
                nums[writepointer] = nums[readpointer]
                readpointer +=1
                writepointer +=1
        return writepointer
        