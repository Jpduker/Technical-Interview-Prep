def missingNumber(nums):
    nums_set=set(nums)
    print(nums_set)
    n=len(nums)+1

    for number in range(0,n):
        if number not in nums_set:
            return number
nums=[0,1,2]
print(missingNumber(nums))