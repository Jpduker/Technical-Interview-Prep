def myAtoi(s):
    res=""
    nums =[0,1,2,3,4,5,6,7,8,9]
    for i in range(0,len(s)):
        if int(s[i]) in nums:
            # if s[0] == "-" or s[0] == "+"" 
            res+=s[i]
        
        
    res=int(res)
    return res
myAtoi("   -42")