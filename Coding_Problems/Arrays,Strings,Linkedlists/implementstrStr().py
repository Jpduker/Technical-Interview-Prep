def strStr(self, haystack: str, needle: str) -> int:
    if needle== "":
        return -1
    
    # haystack ="hello"
    # needle ="ll"
    # len(needle) =2 , len(haystack)=5
    
    for i in range(len(haystack)+1 -len(needle)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1