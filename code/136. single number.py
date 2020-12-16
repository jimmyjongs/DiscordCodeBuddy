# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

# Time Complexity: O(n); single for loop to iterate thru nums; set/dict look up time is O(1)
# Space Complexity: O(n); 1:1 relationship between space allocated and inputs

def singleNum(nums):
    A = set()
    B = set()

    for each in nums:
        if each not in A:
            A.add(each)
        else:
            B.add(each)

    return (A-B).pop()

