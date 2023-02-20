def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    hashmap=defaultdict(int)
    
    paragraph = paragraph.replace(",","")
    paragraph = paragraph.replace(".","")
    paragraph = paragraph.replace("!","")
    paragraph=paragraph.lower()
    print(paragraph)
    paragraph = paragraph.split(" ")
    
    res=0
    
    for i in paragraph:
        hashmap[i]+=1
    for j in hashmap.copy():
        if len(banned) ==0:
            break
        for b in range(len(banned)):
            if j == banned[b]:
                hashmap.pop(j)
    print(hashmap)
    for key, value in hashmap.items():
        res=max(res,value)
    
    for k in hashmap:
        if hashmap[k]==res:
            return k