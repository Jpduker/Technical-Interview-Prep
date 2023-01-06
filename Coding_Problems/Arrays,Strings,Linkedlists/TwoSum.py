def twosum(nums,target):
    hash={}
    for i in range(len(nums)):
        compliment = target -nums[i]
        if compliment in hash:
            return[i,hash[compliment]]
        hash[nums[i]]=i