from collections import defaultdict

def firstUniqChar(self, s: str) -> int:
    hashmap =defaultdict(int)
    
    #add all the character along to the hashmap if it's repeating increase the count by 1.
    for i in s:
        hashmap[i]+=1

    #loop through the hashmap and get the value for the corresponding key "i" of the hashmap
    #when the value is 1 for the first time that is the element of the string which is unique and occurs first 
    #return the index value of the particular substring 
    
    for i in hashmap :
        if hashmap.get(i)==1:
            res=s.index(i)
            return res
    return -1


#Time complexity : O(N) since we go through the string of length N two times.
#Space complexity : O(1) because English alphabet contains 26 letters.