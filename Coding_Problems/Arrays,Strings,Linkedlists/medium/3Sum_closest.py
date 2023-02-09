def threeSumClosest(nums, target):
        
    diff=float('inf')
    nums.sort()
    
    for i in range(0,len(nums)):
        left, right =i+1 ,len(nums)-1
        
        while left<right:
            threeSum = nums[i]+ nums[left] + nums[right]
            
            if abs (target -threeSum )<abs(diff):
                diff = target-threeSum
            if threeSum < target:
                left +=1
            else :
                right -=1
        if diff ==0:
            break
    return  target - diff


nums=[-1,2,1,-4]
target =1
#

print(threeSumClosest(nums, target))