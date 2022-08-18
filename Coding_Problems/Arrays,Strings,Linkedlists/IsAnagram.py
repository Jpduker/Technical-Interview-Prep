def isAnagram(s, t):
    if len(s) != len(t):
        return False
    list = [0]*128
    for i in range(len(s)):
        list[ord(s[i])] += 1
    for j in range(len(t)):
        list[ord(t[j])] -= 1
        if list[ord(t[j])] < 0:
            return False
    return True
