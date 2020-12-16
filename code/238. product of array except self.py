# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].



def products(nums):
    output = [1 for i in range(len(nums))]

    left =  [1 for i in range(len(nums))]
    right = [1 for i in range(len(nums))]

    left[0] = 1
    right[-1] = 1

    for i in range(1, len(nums)):
        left[i] = left[i-1] * nums[i-1]

    for i in range(len(nums)-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]

    for i in range(len(nums)):
        output[i] = left[i] * right[i]
    
    return output


        

    

print(products([4, 5, 1, 8, 2]))
print(products([1,2,3,4]))