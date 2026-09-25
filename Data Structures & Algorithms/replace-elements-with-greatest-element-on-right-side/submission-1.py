class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > max:
                max, arr[i] = arr[i], max
            else:
                arr[i] = max
        return arr
            
            
            

        