# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.



def rob(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[1]

    total = []
    total.append(nums[0])
    total.append(max(nums[1], nums[2]))

    for i in range(2, len(nums), 1):
        total.append(max(nums[i] + total[i - 2], total[i - 1]))

    return total[-1]




nums = [1,2,3,1]
rob(nums)



