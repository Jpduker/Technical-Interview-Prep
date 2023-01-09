def containsDuplicate(nums):   
    hashmap = {}
    for i in range(0,len(nums)):
        print(nums[i] in hashmap)
        if (nums[i] in hashmap):
            return True
        else:
            hashmap[i]=nums[i]
        
    return False
a = containsDuplicate([3,4,3,6])
print(a)