def missingNumber1(nums):
    nums_set=set(nums)
    print(nums_set)
    n=len(nums)+1

    for number in range(0,n):
        if number not in nums_set:
            return number
nums=[0,1,2]
print(missingNumber1(nums))

#Efficient Solution O(nlogn) with space complexity of O(1)

def missingNumber2(nums):
    nums.sort()

    # Ensure that n is at the last index
    if nums[-1] != len(nums):
        return len(nums)
    # Ensure that 0 is at the first index
    elif nums[0] != 0:
        return 0

    # If we get here, then the missing number is on the range (0, n)
    for i in range(1, len(nums)):
        expected_num = nums[i-1] + 1
        if nums[i] != expected_num:
            return expected_num
        
#Most efficient solution using gauss formula to find the expected sum and subtract it from sum(nums)
def missingNumber3(nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum