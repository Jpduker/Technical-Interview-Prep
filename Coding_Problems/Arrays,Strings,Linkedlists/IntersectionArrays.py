from collections import defaultdict
def intersect( nums1, nums2):
    
    hashmap = defaultdict(int)
    res=[]
    if len(nums1) < len(nums2):
        for i in nums1:
            hashmap[i]+=1
            
        for j in nums2:
            if j in hashmap and hashmap.get(j) >0 :
                res.append(j)
                hashmap[j]-=1
    else:
        
        for i in nums2:
            hashmap[i]+=1
            
        for j in nums1:
            if j in hashmap and hashmap.get(j) >0 :
                res.append(j)
                hashmap[j]-=1
    return res
        
        