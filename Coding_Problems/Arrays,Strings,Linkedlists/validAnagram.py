def isAnagram(s, t):
    hashmap={}  
    #Base condition
    if len(s)!=len(t):
        return False 
    #add elements of one string into the hashmap completely
    for i in range(0,len(s)):
        hashmap[s[i]]=1+hashmap.get(s[i],0)   
    
    #Loop through the second hashmap and check if the element   present in 2nd string is in the hashmap
    #if its not present simply return false else return true.
    for j in range(0,len(t)):
        if t[j] not in hashmap:
            return False
        if t[j] in hashmap and not hashmap[t[j]]>0:
            return False
        if t[j] in hashmap and hashmap[t[j]]>0:
            hashmap[t[j]]=1-hashmap.get(t[j],0)
    return True
            
print(isAnagram())
        