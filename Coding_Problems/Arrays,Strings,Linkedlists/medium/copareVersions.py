def compareVersion(version1 , version2):
    
    #split the two strings by dot and add each version in an array 
    nums1= version1.split(".")
    nums2= version2.split(".")
    
    n1=len(nums1)
    n2=len(nums2)
    
    #If the two string's length are not same pad the smaller string with zero's
    
    #loop through the longer string and compare each elem in V1 to each elem in V2
    for i in range(max(n1,n2)):
        i1 = int(nums1[i] if i < n1 else 0)
        i2 = int(nums2[i] if i < n2 else 0)
    
    #if they are not equal then V1 > V2 or V1< V2 wherein we return 1 and -1 respectively
        if i1 != i2:
            return 1 if i1>i2 else  -1
        
    #if the both strings are equal at the end of the loop we return 0
    return 0

version1 ="2.5.33"
version2 ="0.1"

print(compareVersion(version1,version2))