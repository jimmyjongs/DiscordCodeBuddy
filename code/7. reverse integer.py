# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: 
# [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when 
# the reversed integer overflows.

## Start by converting num into a string.

### Convert the string back into an int

def reverse(num: int):
    temp = str(num)
    neg = -len(temp)
    ans = 0
    

    if temp[0] == '-':
        ans = int('-' + temp[:neg:-1])
    else: 
        ans = int(temp[::-1])

    if ans > 2147483647 or ans < -2147483647:
        return 0
    else:
        return ans

print(reverse(-12335))
