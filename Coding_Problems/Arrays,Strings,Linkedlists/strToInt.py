def myAtoi(s):
    
    MAX_INT = 2**31 -1
    MIN_INT =-2**31
    
    i=0
    res=0
    negative =1    
    #whitespaces
    while i<len(s) and s[i]==" ":
        i+=1
    
    # + or - Character 
    if i<len(s) and s[i]=="-" :
        negative =-1
        i+=1
    elif i<len(s) and s[i]=="+":
        i+=1
    hashmap= set("0123456789")
    
    #If we encounter numbers (0 to 9)
    while i<len(s) and s[i] in hashmap:
        print(s[i])
        print(MAX_INT//10)
        if res > (MAX_INT//10) or (res == MAX_INT//10 and int(s[i])> 7):
            if negative==1:
                return MAX_INT 
            else:
                return MIN_INT
             
        res = res*10 + int(s[i])
        i+=1
    
    #if the number is negative it will give the correct sign
 
    return res*negative

print(myAtoi("2147483648"))