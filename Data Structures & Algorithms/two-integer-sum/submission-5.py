class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, x in enumerate(nums):
            hashmap[x] = i

        for i, x in enumerate(nums):
            if (target - x) in hashmap and hashmap[target-x] != i:
                return [i,hashmap[target-x]]
        
        return []

            
        