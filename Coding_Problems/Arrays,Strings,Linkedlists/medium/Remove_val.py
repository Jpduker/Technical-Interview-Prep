def removeElement(nums, val):
    writter =0
    n=len(nums)
    for reader in range(0,n):
        if nums[reader]!=val:
            nums[writter]=nums[reader]
            writter+=1
    return writter

nums=[1,2,3,4,5,2]
val=2

print(removeElement(nums,val))