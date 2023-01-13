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
#Time complexity : O(N) since we go through the string of length N two times.
#Space complexity : O(1) because English alphabet contains 26 letters.