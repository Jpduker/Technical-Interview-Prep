def maxSubarray(nums):
    currSum=maxSum=nums[0]
    for num in nums:
        currSum=max(num , currSum+num)
        maxSum=max(currSum,maxSum)
    return maxSum

nums=[-1,3,-9,5,6,-1,-2,4]

print(maxSubarray(nums))