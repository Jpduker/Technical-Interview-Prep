
#O(n) using O(n) Space 
def rotate_array(nums,k):
    
    length =len(nums)
    res=[0]*length
    for i in range(len(nums)):
        pos=(i+k)%length
        print(pos)
        res[pos] = nums[i]
    return res
            
nums=[1,2,3,4,5,6,7]
k=3

#print(rotate_array(nums,k))


# O(n) solution with O(1) space 

def RotateArray(nums,k):
    k=k%len(nums)
    
    left,right=0,len(nums)-1
    
    #Reversing the entire array first --> [1,2,3,4] ==> [4,3,2,1] assume k=2
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left,right = left+1,right-1
    # we need 2 times rotated array --> [3,4,1,2] as of now we have [4,3,2,1]
    #we also have to reverse the inside two parts also [4,3]-->[3,4] and [2,1]-->[1,2]
    
    left,right=0,k-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left,right = left+1,right-1
    
    left,right=k, len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left,right = left+1,right-1
    return nums

print(RotateArray(nums,k))
     
    