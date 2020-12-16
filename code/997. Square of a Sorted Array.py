# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

# Time Complexity: O(nlogn) due to Timsort
# Space Complexity: O(n), use one unit of space per unit of input

def sortedSquares(nums):
    return sorted([each*each for each in nums])


print(sortedSquares([-7,-3,2,3,11]))