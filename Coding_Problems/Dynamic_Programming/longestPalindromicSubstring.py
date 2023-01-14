def longestPalindrome(s):
    res=''
    resLen=0
    
    for i in range(len(s)):
        left,right=i,i
        
        #odd length string
        while left>=0 and right<len(s) and s[left]==s[right]:
            if (right-left+1) >resLen:      
                res=s[left:right+1]
                resLen=right-left +1
            left-=1
            right+=1
        
        #even length string 
        left,right=i,i+1
        while(left>=0 and right<len(s) and s[left]==s[right]):
            if right-left+1> resLen:
                res=s[left:right+1]
                resLen=right-left+1
            left-=1
            right+=1
    return res
print(longestPalindrome("ababa"))