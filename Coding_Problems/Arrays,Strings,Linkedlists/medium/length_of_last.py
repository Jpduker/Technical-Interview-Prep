def lengthOfLastWord(s: str):
    right,length =len(s) , 0

    while right>0:
        right-=1
        if s[right] !=" ":
            length+=1
        elif length>0:
            return length
    return length

s="elephant bro"


print(lengthOfLastWord(s))
