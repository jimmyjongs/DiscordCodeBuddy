# Given an integer array nums, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets.

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)

def binCount(n):
    counts = []
    for i in range(n**2-1):
        temp = bin(i)[2::]
        
        while len(temp) < n:
            temp = "0" + temp

        counts.append(temp)
    return counts


def subsets(nums):
    counts = binCount(len(nums))
    ans = []

    for each in counts:
        temp = []
        if each[0] == '1':
            temp.append(nums[0])
        if each[1] == '1':
            temp.append(nums[1])
        if each[2] == '1':
            temp.append(nums[2])
        
        ans.append(temp)
    
    return ans


print(subsets([1,2,3]))