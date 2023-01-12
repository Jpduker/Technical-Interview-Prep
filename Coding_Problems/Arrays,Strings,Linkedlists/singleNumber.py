


from collections import defaultdict


def singleNumber(nums):
        
    hashmap =defaultdict(int,{})
    for i in nums:
        hashmap[i]+=1
    print(hashmap)
    for i in hashmap:
        print(hashmap[i])
        if hashmap[i]==1:
            return i
            
            
nums=[2,2,1]

print(singleNumber(nums))

            
        