import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    for i, num in enumerate(nums):
        nums[i] = -num
    heapq.heapify(nums)
    newheap = []
    for i in range(len(nums)):
        heapq.heappush(newheap, heapq.heappop(nums))
    for i in range(len(newheap)):
        newheap[i] *=-1 
    return newheap






# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
