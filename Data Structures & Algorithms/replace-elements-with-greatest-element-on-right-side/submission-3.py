class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] >= max:
                temp = arr[i]
                arr[i] = max
                max = temp
            else:
                arr[i] = max
        return arr
            
            
            

        