from collections import defaultdict

def firstUniqChar(self, s: str) -> int:
    hashmap =defaultdict(int)
    for i in s:
        hashmap[i]+=1

    for i in hashmap :
        if hashmap.get(i)==1:
            res=s.index(i)
            return res
    return -1