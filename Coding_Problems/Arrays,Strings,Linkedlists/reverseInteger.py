def reverse(x):
        string =str(x)
        res=""
        
        if string[0]!= "+" and string[0]!="-" :
            for i in range(len(string)-1,-1,-1):
                res+=string[i]
            if int(res) < pow(2,-31) or int(res) >pow(2,31):
                return 0
            return int(res)
        
        if string[0]=="+" or string[0]=="-":
            res+=string[0]
            for i in range(len(string)-1,0,-1):
                res+=string[i]
            if int(res) <  pow(2,-31) or int(res) >pow(2,31):
                return 0
            return int(res)
                
        return int(res)
print(reverse(10000304))